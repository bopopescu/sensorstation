"""Generated client library for clouduseraccounts version beta."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.clouduseraccounts.beta import clouduseraccounts_beta_messages as messages


class ClouduseraccountsBeta(base_api.BaseApiClient):
  """Generated client library for service clouduseraccounts version beta."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://www.googleapis.com/clouduseraccounts/beta/'

  _PACKAGE = u'clouduseraccounts'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/cloud-platform.read-only', u'https://www.googleapis.com/auth/cloud.useraccounts', u'https://www.googleapis.com/auth/cloud.useraccounts.readonly']
  _VERSION = u'beta'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'ClouduseraccountsBeta'
  _URL_VERSION = u'beta'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new clouduseraccounts handle."""
    url = url or self.BASE_URL
    super(ClouduseraccountsBeta, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.globalAccountsOperations = self.GlobalAccountsOperationsService(self)
    self.groups = self.GroupsService(self)
    self.linux = self.LinuxService(self)
    self.users = self.UsersService(self)

  class GlobalAccountsOperationsService(base_api.BaseApiService):
    """Service class for the globalAccountsOperations resource."""

    _NAME = u'globalAccountsOperations'

    def __init__(self, client):
      super(ClouduseraccountsBeta.GlobalAccountsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Delete(self, request, global_params=None):
      """Deletes the specified operation resource.

      Args:
        request: (ClouduseraccountsGlobalAccountsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ClouduseraccountsGlobalAccountsOperationsDeleteResponse) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'DELETE',
        method_id=u'clouduseraccounts.globalAccountsOperations.delete',
        ordered_params=[u'project', u'operation'],
        path_params=[u'operation', u'project'],
        query_params=[],
        relative_path=u'projects/{project}/global/operations/{operation}',
        request_field='',
        request_type_name=u'ClouduseraccountsGlobalAccountsOperationsDeleteRequest',
        response_type_name=u'ClouduseraccountsGlobalAccountsOperationsDeleteResponse',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Retrieves the specified operation resource.

      Args:
        request: (ClouduseraccountsGlobalAccountsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'clouduseraccounts.globalAccountsOperations.get',
        ordered_params=[u'project', u'operation'],
        path_params=[u'operation', u'project'],
        query_params=[],
        relative_path=u'projects/{project}/global/operations/{operation}',
        request_field='',
        request_type_name=u'ClouduseraccountsGlobalAccountsOperationsGetRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Retrieves the list of operation resources contained within the specified project.

      Args:
        request: (ClouduseraccountsGlobalAccountsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (OperationList) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'clouduseraccounts.globalAccountsOperations.list',
        ordered_params=[u'project'],
        path_params=[u'project'],
        query_params=[u'filter', u'maxResults', u'orderBy', u'pageToken'],
        relative_path=u'projects/{project}/global/operations',
        request_field='',
        request_type_name=u'ClouduseraccountsGlobalAccountsOperationsListRequest',
        response_type_name=u'OperationList',
        supports_download=False,
    )

  class GroupsService(base_api.BaseApiService):
    """Service class for the groups resource."""

    _NAME = u'groups'

    def __init__(self, client):
      super(ClouduseraccountsBeta.GroupsService, self).__init__(client)
      self._upload_configs = {
          }

    def AddMember(self, request, global_params=None):
      """Adds users to the specified group.

      Args:
        request: (ClouduseraccountsGroupsAddMemberRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('AddMember')
      return self._RunMethod(
          config, request, global_params=global_params)

    AddMember.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'clouduseraccounts.groups.addMember',
        ordered_params=[u'project', u'groupName'],
        path_params=[u'groupName', u'project'],
        query_params=[],
        relative_path=u'projects/{project}/global/groups/{groupName}/addMember',
        request_field=u'groupsAddMemberRequest',
        request_type_name=u'ClouduseraccountsGroupsAddMemberRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes the specified Group resource.

      Args:
        request: (ClouduseraccountsGroupsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'DELETE',
        method_id=u'clouduseraccounts.groups.delete',
        ordered_params=[u'project', u'groupName'],
        path_params=[u'groupName', u'project'],
        query_params=[],
        relative_path=u'projects/{project}/global/groups/{groupName}',
        request_field='',
        request_type_name=u'ClouduseraccountsGroupsDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Returns the specified Group resource.

      Args:
        request: (ClouduseraccountsGroupsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Group) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'clouduseraccounts.groups.get',
        ordered_params=[u'project', u'groupName'],
        path_params=[u'groupName', u'project'],
        query_params=[],
        relative_path=u'projects/{project}/global/groups/{groupName}',
        request_field='',
        request_type_name=u'ClouduseraccountsGroupsGetRequest',
        response_type_name=u'Group',
        supports_download=False,
    )

    def Insert(self, request, global_params=None):
      """Creates a Group resource in the specified project using the data included in the request.

      Args:
        request: (ClouduseraccountsGroupsInsertRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Insert')
      return self._RunMethod(
          config, request, global_params=global_params)

    Insert.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'clouduseraccounts.groups.insert',
        ordered_params=[u'project'],
        path_params=[u'project'],
        query_params=[],
        relative_path=u'projects/{project}/global/groups',
        request_field=u'group',
        request_type_name=u'ClouduseraccountsGroupsInsertRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Retrieves the list of groups contained within the specified project.

      Args:
        request: (ClouduseraccountsGroupsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GroupList) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'clouduseraccounts.groups.list',
        ordered_params=[u'project'],
        path_params=[u'project'],
        query_params=[u'filter', u'maxResults', u'orderBy', u'pageToken'],
        relative_path=u'projects/{project}/global/groups',
        request_field='',
        request_type_name=u'ClouduseraccountsGroupsListRequest',
        response_type_name=u'GroupList',
        supports_download=False,
    )

    def RemoveMember(self, request, global_params=None):
      """Removes users from the specified group.

      Args:
        request: (ClouduseraccountsGroupsRemoveMemberRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('RemoveMember')
      return self._RunMethod(
          config, request, global_params=global_params)

    RemoveMember.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'clouduseraccounts.groups.removeMember',
        ordered_params=[u'project', u'groupName'],
        path_params=[u'groupName', u'project'],
        query_params=[],
        relative_path=u'projects/{project}/global/groups/{groupName}/removeMember',
        request_field=u'groupsRemoveMemberRequest',
        request_type_name=u'ClouduseraccountsGroupsRemoveMemberRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class LinuxService(base_api.BaseApiService):
    """Service class for the linux resource."""

    _NAME = u'linux'

    def __init__(self, client):
      super(ClouduseraccountsBeta.LinuxService, self).__init__(client)
      self._upload_configs = {
          }

    def GetAuthorizedKeysView(self, request, global_params=None):
      """Returns a list of authorized public keys for a specific user account.

      Args:
        request: (ClouduseraccountsLinuxGetAuthorizedKeysViewRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LinuxGetAuthorizedKeysViewResponse) The response message.
      """
      config = self.GetMethodConfig('GetAuthorizedKeysView')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetAuthorizedKeysView.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'clouduseraccounts.linux.getAuthorizedKeysView',
        ordered_params=[u'project', u'zone', u'user', u'instance'],
        path_params=[u'project', u'user', u'zone'],
        query_params=[u'instance', u'login'],
        relative_path=u'projects/{project}/zones/{zone}/authorizedKeysView/{user}',
        request_field='',
        request_type_name=u'ClouduseraccountsLinuxGetAuthorizedKeysViewRequest',
        response_type_name=u'LinuxGetAuthorizedKeysViewResponse',
        supports_download=False,
    )

    def GetLinuxAccountViews(self, request, global_params=None):
      """Retrieves a list of user accounts for an instance within a specific project.

      Args:
        request: (ClouduseraccountsLinuxGetLinuxAccountViewsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LinuxGetLinuxAccountViewsResponse) The response message.
      """
      config = self.GetMethodConfig('GetLinuxAccountViews')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetLinuxAccountViews.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'clouduseraccounts.linux.getLinuxAccountViews',
        ordered_params=[u'project', u'zone', u'instance'],
        path_params=[u'project', u'zone'],
        query_params=[u'filter', u'instance', u'maxResults', u'orderBy', u'pageToken'],
        relative_path=u'projects/{project}/zones/{zone}/linuxAccountViews',
        request_field='',
        request_type_name=u'ClouduseraccountsLinuxGetLinuxAccountViewsRequest',
        response_type_name=u'LinuxGetLinuxAccountViewsResponse',
        supports_download=False,
    )

  class UsersService(base_api.BaseApiService):
    """Service class for the users resource."""

    _NAME = u'users'

    def __init__(self, client):
      super(ClouduseraccountsBeta.UsersService, self).__init__(client)
      self._upload_configs = {
          }

    def AddPublicKey(self, request, global_params=None):
      """Adds a public key to the specified User resource with the data included in the request.

      Args:
        request: (ClouduseraccountsUsersAddPublicKeyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('AddPublicKey')
      return self._RunMethod(
          config, request, global_params=global_params)

    AddPublicKey.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'clouduseraccounts.users.addPublicKey',
        ordered_params=[u'project', u'user'],
        path_params=[u'project', u'user'],
        query_params=[],
        relative_path=u'projects/{project}/global/users/{user}/addPublicKey',
        request_field=u'publicKey',
        request_type_name=u'ClouduseraccountsUsersAddPublicKeyRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes the specified User resource.

      Args:
        request: (ClouduseraccountsUsersDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'DELETE',
        method_id=u'clouduseraccounts.users.delete',
        ordered_params=[u'project', u'user'],
        path_params=[u'project', u'user'],
        query_params=[],
        relative_path=u'projects/{project}/global/users/{user}',
        request_field='',
        request_type_name=u'ClouduseraccountsUsersDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Returns the specified User resource.

      Args:
        request: (ClouduseraccountsUsersGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (User) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'clouduseraccounts.users.get',
        ordered_params=[u'project', u'user'],
        path_params=[u'project', u'user'],
        query_params=[],
        relative_path=u'projects/{project}/global/users/{user}',
        request_field='',
        request_type_name=u'ClouduseraccountsUsersGetRequest',
        response_type_name=u'User',
        supports_download=False,
    )

    def Insert(self, request, global_params=None):
      """Creates a User resource in the specified project using the data included in the request.

      Args:
        request: (ClouduseraccountsUsersInsertRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Insert')
      return self._RunMethod(
          config, request, global_params=global_params)

    Insert.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'clouduseraccounts.users.insert',
        ordered_params=[u'project'],
        path_params=[u'project'],
        query_params=[],
        relative_path=u'projects/{project}/global/users',
        request_field=u'user',
        request_type_name=u'ClouduseraccountsUsersInsertRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Retrieves a list of users contained within the specified project.

      Args:
        request: (ClouduseraccountsUsersListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (UserList) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'clouduseraccounts.users.list',
        ordered_params=[u'project'],
        path_params=[u'project'],
        query_params=[u'filter', u'maxResults', u'orderBy', u'pageToken'],
        relative_path=u'projects/{project}/global/users',
        request_field='',
        request_type_name=u'ClouduseraccountsUsersListRequest',
        response_type_name=u'UserList',
        supports_download=False,
    )

    def RemovePublicKey(self, request, global_params=None):
      """Removes the specified public key from the user.

      Args:
        request: (ClouduseraccountsUsersRemovePublicKeyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('RemovePublicKey')
      return self._RunMethod(
          config, request, global_params=global_params)

    RemovePublicKey.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'clouduseraccounts.users.removePublicKey',
        ordered_params=[u'project', u'user', u'fingerprint'],
        path_params=[u'project', u'user'],
        query_params=[u'fingerprint'],
        relative_path=u'projects/{project}/global/users/{user}/removePublicKey',
        request_field='',
        request_type_name=u'ClouduseraccountsUsersRemovePublicKeyRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )
