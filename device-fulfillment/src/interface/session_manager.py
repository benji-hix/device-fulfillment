from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.clipboard import Clipboard
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from src.device_fulfillment.parsers import set_session


def build_session():
    kb = KeyBindings()

    @kb.add('c-c')
    def _(event):
        event.app.exit(exception=KeyboardInterrupt)

    @kb.add('c-v')
    def _(event):
        buffer = event.app.current_buffer
        clipboard = Clipboard()
        text = clipboard.paste()
        buffer.insert_text(text)

    def toolbar():
        toolbar_str = 'Helpful commands:'
        return toolbar_str

    session = PromptSession(
        key_bindings=kb,
        auto_suggest=AutoSuggestFromHistory(),
        bottom_toolbar=toolbar
    )
    set_session(session)
    return session
