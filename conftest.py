import json
import os

import pytest
from playwright.sync_api import Page, BrowserContext
from fixture.ui_facade import UI

env_target = None


@pytest.fixture(scope="function")
def ui(page: Page, context: BrowserContext):
    global env_target
    if env_target is None:
        config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                        ".env")
        with open(config_file_path) as config:
            env_target = json.load(config)
    ui_item = UI(page, context, user=env_target['user'], password=env_target['password'], url=env_target['url'])
    ui_item.page.goto(env_target['url'])
    return ui_item
