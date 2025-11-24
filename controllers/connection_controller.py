from models.user.connection import Connection
from models.user.connection_status import ConnectionStatus
from models.user.user import User
from views.logged_user_view import LoggedUserView
from DAOs.connection_dao import ConnectionDAO

from exceptions.connection_exceptions import (
    InvalidConnectionUsersException,
    UserNotInConnectionException,
)
from exceptions.generic_exceptions import NotFoundException


class ConnectionController:
    def __init__(self, main_controller):
        self.__main_controller = main_controller
        self.__user_view = LoggedUserView()
        self.__connection_dao = ConnectionDAO()

    def load_connections_menu(self):
        while True:
            choice = self.__user_view.show_connections_menu()

            if choice == 0:
                return
            elif choice == 1:
                user_connections = self.__get_user_connections(
                    self.__main_controller.logged_user, ConnectionStatus.ACCEPTED
                )
                con_choice = self.__user_view.show_accepted_connections(
                    user_connections
                )
                if con_choice == 0 or con_choice is None:
                    continue
                else:
                    self.__handle_accepted_connection(
                        con_choice, self.__main_controller.logged_user
                    )
            elif choice == 2:
                self.__handle_pending_requests(self.__main_controller.logged_user)
            elif choice == 3:
                self.__handle_new_connection_request()
            else:
                self.__user_view.show_error_message(
                    ValueError("Invalid option, please select a number from 0 to 3!")
                )

    def accept_connection(self, connection_id: int, user: User):
        connection = self.__find_connection_by_id(connection_id)
        if not connection:
            self.__user_view.show_connection_not_found(connection_id)
            return

        try:
            connection.accept_request(user)
            self.__connection_dao.update(connection)
            self.__user_view.show_operation_done_message()
        except UserNotInConnectionException as e:
            self.__user_view.show_error_message(e)
        except NotFoundException:
            self.__user_view.show_error_message(ValueError("Connection not found."))

    def decline_connection(self, connection_id: int, user: User):
        connection = self.__find_connection_by_id(connection_id)
        if not connection:
            self.__user_view.show_connection_not_found(connection_id)
            return

        try:
            connection.decline_request(user)
            self.__connection_dao.remove(connection.id)
            self.__user_view.show_operation_done_message()
        except (UserNotInConnectionException, NotFoundException) as e:
            self.__user_view.show_error_message(e)

    def __handle_pending_requests(self, logged_user: User):
        pending_requests = []
        all_connections = self.__connection_dao.get_all()

        for connection in all_connections:
            if (
                connection.user2.username == logged_user.username
                and connection.status == ConnectionStatus.PENDING
            ):
                pending_requests.append(connection)

        view_data = []
        for connection in pending_requests:
            view_data.append((connection.id, connection.user1.username))

        while True:
            choice = self.__user_view.show_pending_connection_requests(view_data)

            if choice == 0 or choice is None:
                return

            connection = self.__find_connection_by_id(choice)
            if connection:
                user_requester = connection.user1
                action = self.__user_view.show_accept_reject_connection_menu(
                    user_requester.username
                )

                if action == 1:
                    self.accept_connection(connection.id, logged_user)
                    return
                elif action == 2:
                    self.decline_connection(connection.id, logged_user)
                    return
                elif action == 0:
                    continue
                else:
                    self.__user_view.show_error_message(ValueError("Invalid option!"))
            else:
                self.__user_view.show_connection_not_found(choice)

    def __handle_new_connection_request(self):
        while True:
            try:
                target_username = self.__user_view.show_new_connection_request()
                if target_username == "0":
                    return

                target_user = (
                    self.__main_controller.user_controller.find_user_by_username(
                        target_username
                    )
                )
                if not target_user:
                    self.__user_view.show_error_message(ValueError("User not found."))
                    continue

                self.create_connection(self.__main_controller.logged_user, target_user)
                return
            except (InvalidConnectionUsersException, NotFoundException) as e:
                self.__user_view.show_error_message(e)
                continue

    def __handle_accepted_connection(self, connection_id, logged_user):
        connection = self.__find_connection_by_id(connection_id)

        if not connection:
            self.__user_view.show_connection_not_found(connection_id)
            return

        other_user = (
            connection.user2
            if connection.user1.username == logged_user.username
            else connection.user1
        )

        while True:
            choice = self.__user_view.show_accepted_connection(
                connection.id, logged_user.username, other_user.username
            )

            if choice == 1:
                try:
                    self.__connection_dao.remove(connection.id)
                    self.__user_view.show_operation_done_message()
                except NotFoundException as e:
                    self.__user_view.show_error_message(e)
                return
            elif choice == 0:
                return
            else:
                self.__user_view.show_error_message(ValueError("Invalid option!"))

    def __get_connection_between_users(
        self, user1: User, user2: User
    ) -> Connection | None:
        all_connections = self.__connection_dao.get_all()
        for connection in all_connections:
            if (
                connection.user1.username == user1.username
                and connection.user2.username == user2.username
            ) or (
                connection.user1.username == user2.username
                and connection.user2.username == user1.username
            ):
                return connection
        return None

    def __find_connection_by_id(self, connection_id: int) -> Connection | None:
        try:
            return self.__connection_dao.get(connection_id)
        except KeyError:
            return None

    def __get_user_connections(self, user: User, status: ConnectionStatus):
        user_connections = []
        all_connections = self.__connection_dao.get_all()

        for connection in all_connections:
            if (
                user in [connection.user1, connection.user2]
                and connection.status == status
            ):
                if user == connection.user1:
                    user_connections.append((connection.id, connection.user2.username))
                else:
                    user_connections.append((connection.id, connection.user1.username))
        return user_connections

    def create_connection(self, user1: User, user2: User) -> Connection:
        if user1.username == user2.username:
            raise InvalidConnectionUsersException

        existing_connection = self.__get_connection_between_users(user1, user2)
        if existing_connection:
            self.__user_view.show_connection_already_exists()
            return existing_connection

        new_connection = Connection(user1, user2)
        self.__connection_dao.add(new_connection)
        self.__user_view.show_operation_done_message()
        return new_connection
