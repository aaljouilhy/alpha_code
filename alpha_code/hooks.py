app_name = "alpha_code"
app_title = "Alpha Code"
app_publisher = "alpha_code"
app_description = "Alpha Code System"
app_email = "aaljouilhy@gmail.com"
app_license = "mit"
app_logo_url = "/assets/alpha_code/images/logo-32.png"
# required_apps = []

# Includes in <head>
# ------------------

app_include_css = [
    "/assets/alpha_code/plugins/animate.css/animate.min.css",
    "/assets/alpha_code/plugins/fontawesome/all.min.css",
    "/assets/alpha_code/plugins/tooltip/tooltip-theme-twipsy.css",
    "/assets/alpha_code/plugins/flat-icons/flaticon.css",
    "/assets/alpha_code/css/datavalue_theme.css"
]

app_include_js = [
    "/assets/alpha_code/plugins/nicescroll/nicescroll.js",
    "/assets/alpha_code/plugins/tooltip/tooltip.js",
    "/assets/alpha_code/plugins/jquery-fullscreen/jquery.fullscreen.min.js",
    "/assets/alpha_code/js/vue/side-menu.js",
    "/assets/alpha_code/js/datavalue_theme.js"
]

website_context = {
    "favicon": "/assets/alpha_code/images/logo-icon.png",
    "splash_image": "/assets/alpha_code/images/logo-icon.png"
}

email_brand_image = "assets/alpha_code/images/logo-icon.png"

# include js, css files in header of web template
web_include_css = [
    "assets/css/login.css",
    "assets/alpha_code/css/dv-login.css"
]
web_include_js = [
    "/assets/alpha_code/js/vue/theme-settings.js"
]
#app_include_css = "/assets/alpha_code/css/alpha_code.css"
#app_include_js = ["/assets/alpha_code/js/custom_script.js"]
# include js, css files in header of desk.html
# app_include_css = "/assets/alpha_code/css/alpha_code.css"
# app_include_js = "/assets/alpha_code/js/alpha_code.js"

# include js, css files in header of web template
# web_include_css = "/assets/alpha_code/css/alpha_code.css"
# web_include_js = "/assets/alpha_code/js/alpha_code.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "alpha_code/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "alpha_code/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "alpha_code.utils.jinja_methods",
# 	"filters": "alpha_code.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "alpha_code.install.before_install"
# after_install = "alpha_code.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "alpha_code.uninstall.before_uninstall"
# after_uninstall = "alpha_code.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "alpha_code.utils.before_app_install"
# after_app_install = "alpha_code.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "alpha_code.utils.before_app_uninstall"
# after_app_uninstall = "alpha_code.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "alpha_code.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"alpha_code.tasks.all"
# 	],
# 	"daily": [
# 		"alpha_code.tasks.daily"
# 	],
# 	"hourly": [
# 		"alpha_code.tasks.hourly"
# 	],
# 	"weekly": [
# 		"alpha_code.tasks.weekly"
# 	],
# 	"monthly": [
# 		"alpha_code.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "alpha_code.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "alpha_code.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "alpha_code.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["alpha_code.utils.before_request"]
# after_request = ["alpha_code.utils.after_request"]

# Job Events
# ----------
# before_job = ["alpha_code.utils.before_job"]
# after_job = ["alpha_code.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

user_data_fields = [
    {
        "doctype": "{doctype_1}",
        "filter_by": "{filter_by}",
        "redact_fields": ["{field_1}", "{field_2}"],
        "partial": 1,
    },
    {
        "doctype": "{doctype_2}",
        "filter_by": "{filter_by}",
        "partial": 1,
    },
    {
        "doctype": "{doctype_3}",
        "strict": False,
    },
    {
        "doctype": "{doctype_4}"
    }
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"alpha_code.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

