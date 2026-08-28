"""Owned kit copies — host seams speak APPIC. Isolation: no ux_channel."""
from __future__ import annotations

from components.accordion import Accordion as AccordionCard
from components.actionsheet import ActionSheet as ActionSheetCard
from components.breadcrumb import Breadcrumb as BreadcrumbCard
from components.calendar import Calendar as CalendarCard
from components.carousel import Carousel as CarouselCard
from components.combobox import Combobox as ComboboxCard
from components.command import Command as CommandCard
from components.contextmenu import ContextMenu as ContextMenuCard
from components.dialog import Dialog as DialogCard
from components.dropdown import Dropdown as DropdownCard
from components.login import AuthDecision, Login as LoginCard
from components.otp import Otp as OtpCard
from components.pagination import Pagination as PaginationCard
from components.plans import Plans as PlansCard
from components.pullrefresh import PullRefresh as PullRefreshCard
from components.select import Select as SelectCard
from components.sheet import Sheet as SheetCard
from components.sidebar import Sidebar as SidebarCard
from components.stepper import Stepper as StepperCard
from components.table import Table as TableCard
from components.tabs import Tabs as TabsCard
from components.toast import Toast as ToastCard
from components.typeahead import Typeahead as TypeaheadCard

from appic.store import HOST

__all__ = [
    "AuthDecision",
    "OwnedLogin",
    "OwnedOtp",
    "OwnedSidebar",
    "OwnedBreadcrumb",
    "OwnedTabs",
    "OwnedPull",
    "OwnedAccordion",
    "OwnedCommand",
    "OwnedToast",
    "OwnedTypeahead",
    "OwnedCombobox",
    "OwnedSelect",
    "OwnedDropdown",
    "OwnedSheet",
    "OwnedCarousel",
    "OwnedTable",
    "OwnedPages",
    "OwnedMenu",
    "OwnedSheetActions",
    "OwnedStepper",
    "OwnedPlans",
    "OwnedCalendar",
    "OwnedDialog",
    "KIT_CLASSES",
]


class OwnedLogin(LoginCard):
    id = "login"

    def authenticate(self, *, email: str, password: str, name: str, signup: bool) -> AuthDecision:
        if (email or "").lower().endswith("@blocked.test"):
            HOST.log("login.authenticate", "blocked", "cap")
            return self.Reject("This account is not allowed at the door.", blocked=True)
        HOST.notice = email
        HOST.log("login.authenticate", email, "cap")
        return self.Accept("The door opened" if not signup else "The house wrote your name")


class OwnedOtp(OtpCard):
    id = "otp"

    def on_verify(self, code: str) -> str | None:
        digits = "".join(c for c in (code or "") if c.isdigit())
        if digits == "000000":
            HOST.log("otp.verify", "refused", "cap")
            return None
        HOST.log("otp.verify", digits, "cap")
        return "The seal is warm."


class OwnedSidebar(SidebarCard):
    id = "sidebar"


class OwnedBreadcrumb(BreadcrumbCard):
    id = "breadcrumb"


class OwnedTabs(TabsCard):
    id = "tabs"


class OwnedPull(PullRefreshCard):
    id = "pullrefresh"
    SEED = (
        "Flax shade restocked.",
        "Iron bookend at the bench.",
        "Charcoal stool still drying.",
        "Mira signed the glaze log.",
    )

    def on_refresh(self):
        HOST.log("pullrefresh.refresh", "ledger", "morph")
        have = list(self.items or self.SEED)
        extra = ("House pulse " + str(int(HOST.pulse or 0)),)
        return tuple(extra) + tuple(have)


class OwnedAccordion(AccordionCard):
    id = "accordion"


class OwnedCommand(CommandCard):
    id = "command"
    COMMANDS = (
        ("/", "Open table", "Walk to the table"),
        ("/house", "Open house", "Linen, oak, wool, clay"),
        ("/enter", "Open door", "Login is a Cap"),
        ("/signal", "Open signal", "Swipe, longpress, delay"),
        ("lattice.mint", "Mint a Cap", "Wax seal"),
        ("home.beat", "Pulse the house", "Clock B"),
    )

    def on_run(self, key: str) -> str:
        HOST.log("command.run", key, "morph")
        return key


class OwnedToast(ToastCard):
    id = "toast"


class OwnedTypeahead(TypeaheadCard):
    id = "typeahead"

    def on_pick(self, label: str) -> str:
        HOST.log("typeahead.pick", label, "morph")
        return label


class OwnedCombobox(ComboboxCard):
    id = "combobox"


class OwnedSelect(SelectCard):
    id = "select"


class OwnedDropdown(DropdownCard):
    id = "dropdown"


class OwnedSheet(SheetCard):
    id = "sheet"


class OwnedCarousel(CarouselCard):
    id = "carousel"


class OwnedTable(TableCard):
    id = "table"


class OwnedPages(PaginationCard):
    id = "pagination"


class OwnedMenu(ContextMenuCard):
    id = "contextmenu"

    def on_run(self, key: str) -> str:
        HOST.log("contextmenu.run", key, "morph")
        return key


class OwnedSheetActions(ActionSheetCard):
    id = "actionsheet"
    ACTIONS = (
        ("share", "Share this piece", False),
        ("pin", "Pin to the desk", False),
        ("archive", "Archive (Cap)", True),
    )

    def on_pick(self, key: str) -> str:
        HOST.log("actionsheet.pick", key, "cap" if key == "archive" else "morph")
        return key.replace("-", " ")


class OwnedStepper(StepperCard):
    id = "stepper"

    def on_finish(self) -> str:
        HOST.log("stepper.finish", "visit", "cap")
        return "The visit is placed."


class OwnedPlans(PlansCard):
    id = "plans"

    def on_choose(self, key: str) -> str:
        HOST.log("plans.choose", key, "morph")
        return key


class OwnedCalendar(CalendarCard):
    id = "calendar"

    def on_pick(self, day: str) -> str:
        try:
            HOST.booked = list(HOST.booked or []) + [int(str(day).lstrip("0") or "0")]
        except Exception:
            pass
        HOST.log("calendar.pick", str(day), "morph")
        return str(day)


class OwnedDialog(DialogCard):
    id = "dialog"

    def on_confirm(self, target: str) -> str:
        HOST.log("dialog.confirm", target, "cap")
        return target or "cleared"


KIT_CLASSES = (
    OwnedLogin,
    OwnedOtp,
    OwnedSidebar,
    OwnedBreadcrumb,
    OwnedTabs,
    OwnedPull,
    OwnedAccordion,
    OwnedCommand,
    OwnedToast,
    OwnedTypeahead,
    OwnedCombobox,
    OwnedSelect,
    OwnedDropdown,
    OwnedSheet,
    OwnedCarousel,
    OwnedTable,
    OwnedPages,
    OwnedMenu,
    OwnedSheetActions,
    OwnedStepper,
    OwnedPlans,
    OwnedCalendar,
    OwnedDialog,
)
