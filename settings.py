# -*- coding: utf-8 -*-

import os

from django.utils.translation import ugettext_lazy as _

from horizon.utils import secret_key

from openstack_dashboard.settings import HORIZON_CONFIG

# Force use of native python mysql driver
import pymysql
pymysql.install_as_MySQLdb()


DEBUG = True

# This setting controls whether or not compression is enabled. Disabling
# compression makes Horizon considerably slower, but makes it much easier
# to debug JS and CSS changes
COMPRESS_ENABLED = True

# This setting controls whether compression happens on the fly, or offline
# with `python manage.py compress`
# See https://django-compressor.readthedocs.io/en/latest/usage/#offline-compression
# for more information
COMPRESS_OFFLINE = True

# WEBROOT is the location relative to Webserver root
# should end with a slash.
WEBROOT = '/'

SHOW_KEYSTONE_V2_RC = False
LOCAL_PATH = os.path.dirname(os.path.abspath(__file__))

#
# TODO(tres): Remove these once Keystone has an API to identify auth backend.
OPENSTACK_KEYSTONE_BACKEND = {
    'name': 'native',
    'can_edit_user': True,
    'can_edit_group': True,
    'can_edit_project': True,
    'can_edit_domain': True,
    'can_edit_role': True,
}

# A dictionary of settings which can be used to provide the default values for
# properties found in the Launch Instance modal.
LAUNCH_INSTANCE_DEFAULTS = {
    'config_drive': False,
    'create_volume': False,
    'disable_image': False,
    'disable_instance_snapshot': False,
    'disable_volume': False,
    'disable_volume_snapshot': False,
    'enable_scheduler_hints': False,
    'hide_create_volume': True,
}

# The Xen Hypervisor has the ability to set the mount point for volumes
# attached to instances (other Hypervisors currently do not). Setting
# can_set_mount_point to True will add the option to set the mount point
# from the UI.
OPENSTACK_HYPERVISOR_FEATURES = {
    'can_set_mount_point': False,
    'can_set_password': True,
    'requires_keypair': False,
    'enable_quotas': True
}

# The OPENSTACK_CINDER_FEATURES settings can be used to enable optional
# services provided by cinder that is not exposed by its extension API.
OPENSTACK_CINDER_FEATURES = {
    'enable_backup': True,
}

# The OPENSTACK_NEUTRON_NETWORK settings can be used to enable optional
# services provided by neutron. Options currently available are load
# balancer service, security groups, quotas, VPN service.
OPENSTACK_NEUTRON_NETWORK = {
    'enable_router': True,
    'enable_quotas': True,
    'enable_ipv6': False,
    'enable_distributed_router': False,
    'enable_ha_router': False,
    'enable_fip_topology_check': True,

    # Default dns servers you would like to use when a subnet is
    # created.  This is only a default, users can still choose a different
    # list of dns servers when creating a new subnet.
    # The entries below are examples only, and are not appropriate for
    # real deployments
    'default_dns_nameservers': ["8.8.8.8", "8.8.4.4"],

    # Set which VNIC types are supported for port binding. Only the VNIC
    # types in this list will be available to choose from when creating a
    # port.
    # VNIC types include 'normal', 'direct', 'direct-physical', 'macvtap',
    # 'baremetal' and 'virtio-forwarder'
    # Set to empty list or None to disable VNIC type selection.
    'supported_vnic_types': [],

    # Set list of available physical networks to be selected in the physical
    # network field on the admin create network modal. If it's set to an empty
    # list, the field will be a regular input field.
    # e.g. ['default', 'test']
    'physical_networks': [],

}

# The IMAGE_CUSTOM_PROPERTY_TITLES settings is used to customize the titles for
# image custom property attributes that appear on image detail pages.
IMAGE_CUSTOM_PROPERTY_TITLES = {
    "architecture": _("Architecture"),
    "kernel_id": _("Kernel ID"),
    "ramdisk_id": _("Ramdisk ID"),
    "image_state": _("Euca2ools state"),
    "project_id": _("Project ID"),
    "image_type": _("Image Type"),
}

# The IMAGE_RESERVED_CUSTOM_PROPERTIES setting is used to specify which image
# custom properties should not be displayed in the Image Custom Properties
# table.
IMAGE_RESERVED_CUSTOM_PROPERTIES = []

# The number of objects (Swift containers/objects or images) to display
# on a single page before providing a paging element (a "more" link)
# to paginate results.
API_RESULT_LIMIT = 1000
API_RESULT_PAGE_SIZE = 50

# The size of chunk in bytes for downloading objects from Swift
SWIFT_FILE_TRANSFER_CHUNK_SIZE = 512 * 1024

# The default number of lines displayed for instance console log.
INSTANCE_LOG_LENGTH = 35

# Specify a maximum number of items to display in a dropdown.
DROPDOWN_MAX_ITEMS = 100

# The timezone of the server. This should correspond with the timezone
# of your entire OpenStack installation, and hopefully be in UTC.
TIME_ZONE = "UTC"

# Path to directory containing policy.json files
POLICY_FILES_PATH = '/src/nectar-dashboard/policy'

# Map of local copy of service policy files.
# Please insure that your identity policy file matches the one being used on
# your keystone servers. There is an alternate policy file that may be used
# in the Keystone v3 multi-domain case, policy.v3cloudsample.json.
# This file is not included in the Horizon repository by default but can be
# found at
# http://git.openstack.org/cgit/openstack/keystone/tree/etc/ \
# policy.v3cloudsample.json
# Having matching policy files on the Horizon and Keystone servers is essential
# for normal operation. This holds true for all services and their policy files.
POLICY_FILES = {
    'identity': 'keystone_policy.json',
    'compute': 'nova_policy.json',
    'volume': 'cinder_policy.json',
    'image': 'glance_policy.json',
    'network': 'neutron_policy.json',
    'orchestration': 'heat_policy.json',
    'murano': 'murano_policy.json',
    'dns': 'designate_policy.json',
}

# Change this patch to the appropriate list of tuples containing
# a key, label and static directory containing two files:
# _variables.scss and _styles.scss
AVAILABLE_THEMES = [
    ('default', 'Default', 'themes/default'),
    ('nectar', 'Nectar', '/src/nectar-dashboard/theme'),
]

SELECTABLE_THEMES = [
    ('nectar', 'Nectar', '/src/nectar-dashboard/theme'),
]

DEFAULT_THEME = 'nectar'

HORIZON_CONFIG["customization_module"] = "nectar_dashboard.overrides"

LOGGING = {
    'version': 1,
    # When set to True this will disable all logging except
    # for loggers specified in this configuration dictionary. Note that
    # if nothing is specified here and disable_existing_loggers is True,
    # django.db.backends will still log unless it is disabled explicitly.
    'disable_existing_loggers': False,
    # If apache2 mod_wsgi is used to deploy OpenStack dashboard
    # timestamp is output by mod_wsgi. If WSGI framework you use does not
    # output timestamp for logging, add %(asctime)s in the following
    # format definitions.
    'formatters': {
        'console': {
            'format': '%(levelname)s %(name)s %(message)s'
        },
        'operation': {
            # The format of "%(message)s" is defined by
            # OPERATION_LOG_OPTIONS['format']
            'format': '%(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            # Set the level to "DEBUG" for verbose output logging.
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
        'operation': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'operation',
        },
        'file': {
            'filename': '/logs/debug',
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        'horizon': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'horizon.operation_log': {
            'handlers': ['operation'],
            'level': 'INFO',
            'propagate': False,
        },
        'openstack_dashboard': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'nectar_dashboard': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'novaclient': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'cinderclient': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'keystoneauth': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'keystoneclient': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'glanceclient': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'neutronclient': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'swiftclient': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'oslo_policy': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'openstack_auth': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'nose.plugins.manager': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # Logging from django.db.backends is VERY verbose, send to null
        # by default.
        'django.db.backends': {
            'handlers': ['null'],
            'propagate': False,
        },
        'requests': {
            'handlers': ['null'],
            'propagate': False,
        },
        'urllib3': {
            'handlers': ['null'],
            'propagate': False,
        },
        'chardet.charsetprober': {
            'handlers': ['null'],
            'propagate': False,
        },
        'iso8601': {
            'handlers': ['null'],
            'propagate': False,
        },
        'scss': {
            'handlers': ['null'],
            'propagate': False,
        },
    },
}

# 'direction' should not be specified for all_tcp/udp/icmp.
# It is specified in the form.
SECURITY_GROUP_RULES = {
    'all_icmp': {
        'name': _('All ICMP'),
        'ip_protocol': 'icmp',
        'from_port': '-1',
        'to_port': '-1',
    },
    'ssh': {
        'name': 'SSH',
        'ip_protocol': 'tcp',
        'from_port': '22',
        'to_port': '22',
    },
    'dns': {
        'name': 'DNS',
        'ip_protocol': 'tcp',
        'from_port': '53',
        'to_port': '53',
    },
    'http': {
        'name': 'HTTP',
        'ip_protocol': 'tcp',
        'from_port': '80',
        'to_port': '80',
    },
    'https': {
        'name': 'HTTPS',
        'ip_protocol': 'tcp',
        'from_port': '443',
        'to_port': '443',
    },
    'ms_sql': {
        'name': 'MS SQL',
        'ip_protocol': 'tcp',
        'from_port': '1433',
        'to_port': '1433',
    },
    'mysql': {
        'name': 'MYSQL',
        'ip_protocol': 'tcp',
        'from_port': '3306',
        'to_port': '3306',
    },
    'postgresql': {
        'name': 'PostgreSQL',
        'ip_protocol': 'tcp',
        'from_port': '5432',
        'to_port': '5432',
    },
    'rdp': {
        'name': 'RDP',
        'ip_protocol': 'tcp',
        'from_port': '3389',
        'to_port': '3389',
    },
}
# AngularJS requires some settings to be made available to
# the client side. Some settings are required by in-tree / built-in horizon
# features. These settings must be added to REST_API_REQUIRED_SETTINGS in the
# form of ['SETTING_1','SETTING_2'], etc.
#
# You may remove settings from this list for security purposes, but do so at
# the risk of breaking a built-in horizon feature. These settings are required
# for horizon to function properly. Only remove them if you know what you
# are doing. These settings may in the future be moved to be defined within
# the enabled panel configuration.
# You should not add settings to this list for out of tree extensions.
# See: https://wiki.openstack.org/wiki/Horizon/RESTAPI
REST_API_REQUIRED_SETTINGS = ['OPENSTACK_HYPERVISOR_FEATURES',
                              'LAUNCH_INSTANCE_DEFAULTS',
                              'OPENSTACK_IMAGE_FORMATS',
                              'OPENSTACK_KEYSTONE_DEFAULT_DOMAIN',
                              'CREATE_IMAGE_DEFAULTS']

# Help URL can be made available for the client. To provide a help URL, edit the
# following attribute to the URL of your choice.
HORIZON_CONFIG["help_url"] = "http://support.nectar.org.au/"

# RCallocations plugin has a page to provide extra informatation for warnings
# about quota and other inconsistencies in an allocation request.
HORIZON_CONFIG["WARNING_INFO_URL"] = "https://support.ehelp.edu.au/support/solutions/articles/6000220088"

####################
# NeCTAR settings  #
####################
import urllib

ADMINS = (
    ('Admin', 'admin@example.com'),
)
MANAGERS = ADMINS

NECTAR_DEFAULT_NETWORK_ENABLED = True
NECTAR_NETWORK_PROVIDER_FILTER = 'midonet'

OPENSTACK_PREPROD_CELLS = [""]
OPENSTACK_PREPROD_ROLE = "admin"

KEYSTONE_MEMBER_ROLE_ID = ''
KEYSTONE_ADMIN_ENDPOINT_PERMS = ('openstack.roles.tenantmanager',)

USER_INFO_LOOKUP_ROLES = [('openstack.roles.allocationadmin',
                           'openstack.roles.operator',
                           'openstack.roles.helpdesk',
                           'openstack.roles.admin')]

# following is the comma separated list of people who are to receive
# e-mail when an allocation request is submitted
ALLOCATION_EMAIL_RECIPIENTS = ("allocations@example.com", )
ALLOCATION_EMAIL_FROM = "allocations@example.com"
ALLOCATION_EMAIL_REPLY_TO = "support@example.com"
ALLOCATION_EMAIL_BCC_RECIPIENTS = []

ALLOCATION_GLOBAL_READ_ROLES = ['read_only', 'admin', 'monitoring']
ALLOCATION_GLOBAL_ADMIN_ROLES = ['admin', 'provisioner']
ALLOCATION_APPROVER_ROLES = ['allocationadmin', 'admin']

ALLOCATION_HOME_ZONE_MAPPINGS = {
    'auckland': ['auckland'],
    'ersa': ['sa'],
    'intersect': ['intersect'],
    'monash': ['monash-01', 'monash-02', 'monash-03'],
    'nci': ['NCI'],
    'qcif': ['QRIScloud'],
    'swinburne': ['swinburne-01'],
    'tpac': ['tasmania', 'tasmania-s'],
    'uom': ['melbourne-qh2-uom'],
}

# Mappings for storage (volume and share) zones
ALLOCATION_HOME_STORAGE_ZONE_MAPPINGS = {
    'auckland': ['auckland'],
    'ersa': ['sa'],
    'intersect': ['intersect'],
    'monash': ['monash-02-cephfs', 'monash'],
    'nci': ['NCI'],
    'qcif': ['QRIScloud-GPFS', 'QRIScloud', 'QRIScloud-RDS'],
    'swinburne': ['swinburne'],
    'tpac': ['tasmania'],
    'uom': ['melbourne'],
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS':
    'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 1000,
    'DEFAULT_FILTER_BACKENDS':
    ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_AUTHENTICATION_CLASSES':
    (
        'nectar_dashboard.rest_auth.CsrfExemptSessionAuthentication',
        'nectar_dashboard.rest_auth.KeystoneAuthentication',
    ),
}

ADD_INSTALLED_APPS = [
    'rest_framework',
    'django_filters',
    'corsheaders',
    'select2',
]

REST_VIEW_SETS = (
    ('allocations', 'nectar_dashboard.rcallocation.api.AllocationViewSet', None),
    ('quotas', 'nectar_dashboard.rcallocation.api.QuotaViewSet', None),
    ('chiefinvestigators', 'nectar_dashboard.rcallocation.api.ChiefInvestigatorViewSet', None),
    ('institutions', 'nectar_dashboard.rcallocation.api.InstitutionViewSet', None),
    ('publications', 'nectar_dashboard.rcallocation.api.PublicationViewSet', None),
    ('grants', 'nectar_dashboard.rcallocation.api.GrantViewSet', None),
    ('resources', 'nectar_dashboard.rcallocation.api.ResourceViewSet', None),
    ('zones', 'nectar_dashboard.rcallocation.api.ZoneViewSet', None),
    ('service-types', 'nectar_dashboard.rcallocation.api.ServiceTypeViewSet', None),
    ('sites', 'nectar_dashboard.rcallocation.api.SiteViewSet', None),
    ('approvers', 'nectar_dashboard.rcallocation.api.ApproverViewSet', None),
    ('for-codes', 'nectar_dashboard.rcallocation.api.for.FORViewSet', 'for-codes'),
    ('for-tree', 'nectar_dashboard.rcallocation.api.for.AllocationTreeViewSet', 'for-tree'),
)


CORES_RESOURCE_ID = 47
INSTANCE_RESOURCE_ID = 53

# Disable getting console in network topology view as it is a massive performance hit
CONSOLE_TOPOLOGY_ENABLED = False

SESSION_TIMEOUT = 21600  # 6 hours

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

MIDDLEWARE = (
    'corsheaders.middleware.CorsMiddleware',
    'openstack_auth.middleware.OpenstackAuthMonkeyPatchMiddleware',
    'debreach.middleware.RandomCommentMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'horizon.middleware.OperationLogMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'horizon.middleware.HorizonMiddleware',
    'horizon.themes.ThemeMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'openstack_dashboard.contrib.developer.profiler.middleware.'
    'ProfilerClientMiddleware',
    'openstack_dashboard.contrib.developer.profiler.middleware.'
    'ProfilerMiddleware',
)

CORS_URLS_REGEX = r'^/rest_api/.*$'
CORS_ALLOW_METHODS = (
        'GET',
        'OPTIONS',
)

# If horizon is running in production (DEBUG is False), set this
# with the list of host/domain names that the application can serve.
# For more information see:
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    '*'
]

# The absolute path to the directory where message files are collected.
# The message file must have a .json file extension. When the user logins to
# horizon, the message files collected are processed and displayed to the user.
MESSAGES_PATH='/tmp/'
STATIC_ROOT = '/static'
SECRET_KEY = 'test'


# Enables keystone web single-sign-on if set to True.
WEBSSO_ENABLED = False


# The Murano plugin still requires this.
HORIZON_CONFIG['legacy_static_settings'] = False
