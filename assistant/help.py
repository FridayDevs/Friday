


from main_startup.core.decorators import friday_on_cmd as skem
from main_startup.core.startup_helpers import run_cmd
from main_startup.helper_func.basic_helpers import edit_or_reply, get_text
from main_startup.__main__ import bot


@skem(
    ["help", "helper"],
    cmd_help={
        "help": "Gets Help Menu",
        "example": "{ch}help",
    },
)
async def help(client, message):
    starkbot = await bot.get_me()
    bot_username = starkbot.username
    nice = await client.get_inline_bot_results(bot=bot_username, query="help")
    await client.send_inline_bot_result(message.chat.id, nice.query_id, nice.results[0].id, hide_via=True)
    await message.delete()
