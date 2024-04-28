import streamlit as st
from client_pages.utils import *
from streamlit_option_menu import option_menu
from client_pages.dialogue.dialogue import dialogue_page, chat_box
from client_pages.knowledge_base.knowledge_base import knowledge_base_page
import client_pages.styles as css
import os
import sys
from server.utils import api_address


api = ApiRequest(base_url=api_address())

if __name__ == "__main__":
    is_lite = "lite" in sys.argv

    st.set_page_config(
        "日照城投智能聊天系统",
        os.path.join("img", "chatchat_icon_blue_square_v2.png"),
        initial_sidebar_state="expanded",
        menu_items=None
    )
    css.common()

    pages = {
        "对话": {
            "icon": "chat",
            "func": dialogue_page,
        },
        # "知识库管理": {
        #     "icon": "hdd-stack",
        #     "func": knowledge_base_page,
        # },
    }

    with st.sidebar:
        st.image(
            os.path.join(
                "img",
                "logo-long-chatchat-trans-v2.png"
            ),
            width=200,
            use_column_width=False
        )
        options = list(pages)
        icons = [x["icon"] for x in pages.values()]

        default_index = 0
        selected_page = option_menu(
            "",
            options=options,
            icons=icons,
            # menu_icon="chat-quote",
            default_index=default_index,
            orientation="horizontal",
            styles={
                "container": {"width": "280px"}
            }
        )

    if selected_page in pages:
        pages[selected_page]["func"](api=api, is_lite=is_lite)
