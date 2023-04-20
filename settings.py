# -*- coding: utf-8 -*-

import os

from django.utils.translation import ugettext_lazy as _

from horizon.utils import secret_key

from openstack_dashboard.settings import HORIZON_CONFIG

# Force use of native python mysql driver
# import pymysql
# pymysql.install_as_MySQLdb()


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


# A dictionary of settings which can be used to provide the default values for
# properties found in the Launch Instance modal.
LAUNCH_INSTANCE_DEFAULTS = {
    'config_drive': False,
    'enable_scheduler_hints': False,
    'create_volume': False,
    'disable_image': False,
    'disable_instance_snapshot': False,
    'disable_volume': False,
    'disable_volume_snapshot': False,
    'create_volume': False,
    'enable_scheduler_hints': False,
    'hide_create_volume': True,
    'config_drive': False,
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
    'default_dns_nameservers': ["1.1.1.1", "1.0.0.1"],

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


# The IMAGE_RESERVED_CUSTOM_PROPERTIES setting is used to specify which image
# custom properties should not be displayed in the Image Custom Properties
# table.
IMAGE_RESERVED_CUSTOM_PROPERTIES = [
    'os_hash_algo',
    'os_hash_value',
    'os_hidden'
]

# The number of objects (Swift containers/objects or images) to display
# on a single page before providing a paging element (a "more" link)
# to paginate results.
API_RESULT_LIMIT = 1000
API_RESULT_PAGE_SIZE = 50

# Specify a maximum number of items to display in a dropdown.
DROPDOWN_MAX_ITEMS = 100

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
    'dns': 'designate_policy.yaml',
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
            'level': 'INFO',
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

# Help URL can be made available for the client. To provide a help URL, edit the
# following attribute to the URL of your choice.
HORIZON_CONFIG["help_url"] = "http://support.nectar.org.au/"

# RCallocations plugin has a page to provide extra informatation for warnings
# about quota and other inconsistencies in an allocation request.
HORIZON_CONFIG["WARNING_INFO_URL"] = "https://support.ehelp.edu.au/support/solutions/articles/6000220088"

# RCallocations plugin has an approver button to open a browser page
# with the Freshdesk tickets for a given allocation.
HORIZON_CONFIG['FRESHDESK_SEARCH_URL'] = (
    "https://support.ehelp.edu.au/a/tickets/filters/search"
    "?orderBy=updated_at&orderType=desc&ref=_created")

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


# Allocation notifier choices: 'freshdesk' and 'smtp'
ALLOCATION_NOTIFIER = 'freshdesk'

# Freshdesk details for ticket interactions and / or email outbounding
FRESHDESK_DOMAIN = "fixme.freshdesk.com"
FRESHDESK_KEY = "fixme"
FRESHDESK_GROUP_ID = "1111"
FRESHDESK_EMAIL_CONFIG_ID = "3333"

# Following are the people who are to receive e-mail when an
# allocation request or amendment is submitted
ALLOCATION_EMAIL_RECIPIENTS = ("allocations@example.com", )
ALLOCATION_EMAIL_FROM = "allocations@example.com"
ALLOCATION_EMAIL_REPLY_TO = "support@example.com"
ALLOCATION_EMAIL_CC_RECIPIENTS = []
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

# Mappings from sites to member organization.
# (Source: https://wiki.rc.nectar.org.au/wiki/NodeMemberOrganizations)
SITE_MEMBERS_MAPPING = {
    'ardc': ['ardc.edu.au'],
    'auckland': ['auckland.edu.nz'],
    'ersa': [],
    'intersect': ['acu.edu.au', 'adelaide.edu.au', 'canberra.edu.au',
                  'deakin.edu.au', 'latrobe.edu.au', 'scu.edu.au',
                  'une.edu.au', 'unisa.edu.au', 'unsw.edu.au', 'uts.edu.au',
                  'westernsydney.edu.au', 'saxinstitute.org.au',
                  'sirca.org.au', 'intersect.org.au'],
    'monash': ['monash.edu', 'rmit.edu.au'],
    'nci': [],
    'qcif': ['uq.edu.au', 'qut.edu.au', 'griffith.edu.au',
             'cqu.edu.au', 'usq.edu.au', 'usc.edu.au', 'jcu.edu.au',
             'bond.edu.au', 'qcif.edu.au', 'csiro.au'],
    'swinburne': ['swin.edu.au', 'swinburne.edu.au'],
    'tpac': ['utas.edu.au', 'aapartnership.org.au', 'bom.gov.au',
             'csiro.au', 'antarctica.gov.au'],
    'uom': ['unimelb.edu.au', 'florey.edu.au', 'bionicsinstitute.org',
            'cera.org.au', 'cr2cr.com.au', 'mentalhealthcrc.com',
            'petermac.org', 'svhm.org.au', 'wehi.edu.au',
            'metabolomics.net.au', 'mcri.edu.au', 'viccompcancerctr.org',
            'cancercrc.com', 'cancervic.org.au', 'mbs.edu'],
}

# FoR code series allowed for new allocations and amendments.  The series
# names are defined in forcodes.py file.
ALLOCATION_FOR_CODE_SERIES = "ANZSRC_2020"

# URI for the ROR dump file for the 0070 / 0071 migrations that load the
# Organisations table, load local additions, and convert institution
# strings to organisation refs.  It the URI is a URL, it will be fetched
# locally and cached in the current directory.  If it is a relative URI
# (i.e. no protocol) it is interpreted as a local pathname.  If it is None,
# these migrations are no-ops.
ORGANISATION_MIGRATION_ROR_DUMP_URI = \
    "https://object-store.rc.nectar.org.au" \
    "/v1/AUTH_2f6f7e75fc0f453d9c127b490b02e9e3/dashboard-ror-dumps/" \
    "v1.20-2023-02-28-ror-data.json"

# If the following setting is True, any unmappable institution strings
# will cause the 0071 migration to fail.  If False, they will be quietly
# mapped to "Unknown Organization"
ORGANISATION_MIGRATION_STRICT = True

# Disable getting console in network topology view as it is a massive performance hit
CONSOLE_TOPOLOGY_ENABLED = False

SESSION_TIMEOUT = 21600  # 6 hours

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

MIDDLEWARE = (
    'nectar_dashboard.middleware.healthcheck_middleware',
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
