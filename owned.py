"""Register owned kit copies onto the App.

Product owns ``components/``. Never ``from ux_compose.kit import Login``.
Drawer is a Sheet alias — given its own id so both rooms can be walked.
"""
from __future__ import annotations

from typing import Any

from components.accordion import Accordion
from components.actionsheet import ActionSheet
from components.alert import Alert
from components.alertdialog import AlertDialog
from components.attachment import Attachment
from components.avatar import Avatar
from components.badge import Badge
from components.banner import Banner
from components.bottomnav import BottomNav
from components.breadcrumb import Breadcrumb
from components.calendar import Calendar
from components.card import Card
from components.carousel import Carousel
from components.chart import Chart
from components.chat import Chat
from components.colorpicker import ColorPicker
from components.combobox import Combobox
from components.command import Command
from components.contextmenu import ContextMenu
from components.countdown import Countdown
from components.cta import Cta
from components.datepicker import DatePicker
from components.descriptionlist import DescriptionList
from components.dialog import Dialog
from components.diff import Diff
from components.drawer import Drawer
from components.dropdown import Dropdown
from components.emptystate import EmptyState
from components.fab import Fab
from components.featuregrid import FeatureGrid
from components.feed import Feed
from components.fieldset import Fieldset
from components.fileupload import FileUpload
from components.filterbar import FilterBar
from components.footer import Footer
from components.formlayout import FormLayout
from components.hero import Hero
from components.hovercard import HoverCard
from components.login import AuthDecision, Login
from components.logocloud import LogoCloud
from components.menubar import Menubar
from components.mockup import Mockup
from components.multiselect import MultiSelect
from components.navbar import Navbar
from components.navmenu import NavMenu
from components.newsletter import Newsletter
from components.otp import Otp
from components.pagination import Pagination
from components.plans import Plans
from components.popover import Popover
from components.pricingsection import PricingSection
from components.progress import Progress
from components.pullrefresh import PullRefresh
from components.questionnaire import Questionnaire
from components.rating import Rating
from components.resizable import Resizable
from components.scrollarea import ScrollArea
from components.searchbar import SearchBar
from components.select import Select
from components.separator import Separator
from components.sheet import Sheet
from components.sidebar import Sidebar
from components.skeleton import Skeleton
from components.slider import Slider
from components.spinbutton import SpinButton
from components.stats import Stats
from components.stepper import Stepper
from components.switch import Switch
from components.table import Table
from components.tabs import Tabs
from components.tagsinput import TagsInput
from components.testimonials import Testimonials
from components.themeswitch import ThemeSwitch
from components.timeline import Timeline
from components.toast import Toast
from components.togglegroup import ToggleGroup
from components.toolbar import Toolbar
from components.tooltip import Tooltip
from components.tree import Tree
from components.typeahead import Typeahead
from components.usermenu import UserMenu


class DrawerRail(Drawer):
    """Sheet alias with its own surface id so /house can sight both edges."""

    id = "drawer"


class FoundryLogin(Login):
    """Door login. Submit spends auth.login / auth.signup against the Host."""

    id = "login"

    def authenticate(self, email: str, password: str, *, signup: bool = False):
        from store import HOST

        mail = (email or "").strip().lower()
        if mail.endswith("@blocked.test"):
            return AuthDecision(False, "This mark is refused.", blocked=True)
        if "@" not in mail or len(password or "") < 8:
            return AuthDecision(False, "The door stays shut.")
        HOST.authed = True
        HOST.member = mail.split("@")[0]
        return AuthDecision(True, f"Welcome, {HOST.member}.")


KIT_CLASSES: list[type] = [
    FoundryLogin,
    Otp,
    UserMenu,
    Dialog,
    Sheet,
    DrawerRail,
    ActionSheet,
    AlertDialog,
    Command,
    Dropdown,
    Popover,
    Tooltip,
    HoverCard,
    ContextMenu,
    NavMenu,
    Select,
    Combobox,
    Table,
    Pagination,
    Accordion,
    Tabs,
    Carousel,
    Calendar,
    Sidebar,
    Breadcrumb,
    Stepper,
    Tree,
    Feed,
    ScrollArea,
    FormLayout,
    Fieldset,
    DatePicker,
    Switch,
    Slider,
    TagsInput,
    MultiSelect,
    FileUpload,
    Attachment,
    Typeahead,
    SearchBar,
    FilterBar,
    Questionnaire,
    Newsletter,
    Hero,
    Cta,
    Footer,
    Card,
    EmptyState,
    Stats,
    Alert,
    Banner,
    Progress,
    Skeleton,
    Avatar,
    Badge,
    FeatureGrid,
    Testimonials,
    LogoCloud,
    PricingSection,
    Plans,
    Rating,
    Timeline,
    Chart,
    Resizable,
    ColorPicker,
    Fab,
    Diff,
    Countdown,
    Mockup,
    Chat,
    Navbar,
    Menubar,
    Toolbar,
    ToggleGroup,
    SpinButton,
    ThemeSwitch,
    BottomNav,
    Separator,
    Toast,
    PullRefresh,
    DescriptionList,
]

WINGS: dict[str, tuple[str, tuple[str, ...]]] = {
    "door": ("Door", ("login", "otp", "usermenu")),
    "edge": ("Edge", ("dialog", "sheet", "drawer", "actionsheet", "alertdialog", "command")),
    "anchored": (
        "Anchored",
        ("dropdown", "popover", "tooltip", "hovercard", "contextmenu", "navmenu", "select", "combobox"),
    ),
    "collection": (
        "Collection",
        (
            "table",
            "pagination",
            "accordion",
            "tabs",
            "carousel",
            "calendar",
            "sidebar",
            "breadcrumb",
            "stepper",
            "tree",
            "feed",
            "scrollarea",
        ),
    ),
    "form": (
        "Form",
        (
            "formlayout",
            "fieldset",
            "datepicker",
            "switch",
            "slider",
            "tagsinput",
            "multiselect",
            "fileupload",
            "attachment",
            "typeahead",
            "searchbar",
            "filterbar",
            "questionnaire",
            "newsletter",
        ),
    ),
    "market": (
        "Market",
        (
            "hero",
            "cta",
            "footer",
            "card",
            "emptystate",
            "stats",
            "alert",
            "banner",
            "progress",
            "skeleton",
            "avatar",
            "badge",
            "featuregrid",
            "testimonials",
            "logocloud",
            "pricingsection",
            "plans",
            "rating",
            "timeline",
            "descriptionlist",
        ),
    ),
    "forge": (
        "Forge",
        ("chart", "resizable", "colorpicker", "fab", "diff", "countdown", "mockup", "chat"),
    ),
    "chrome": (
        "Chrome",
        ("navbar", "menubar", "toolbar", "togglegroup", "spinbutton", "themeswitch", "bottomnav", "separator"),
    ),
    "presence": ("Presence", ("toast", "pullrefresh")),
}


def register_kits(app: Any) -> dict[str, Any]:
    registry: dict[str, Any] = {}
    for cls in KIT_CLASSES:
        try:
            app.add(cls)
        except Exception:
            continue
    behavior = getattr(app, "behavior", None) or getattr(app, "_behavior", None)
    if behavior is not None and hasattr(behavior, "components"):
        try:
            registry.update(dict(behavior.components()))
        except Exception:
            pass
    app._kit_registry = registry
    return registry
