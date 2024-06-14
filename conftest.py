import json
import os

import pytest
from playwright.sync_api import Page, BrowserContext
from core.ui_facade import UI


@pytest.fixture(scope="function")
def ui(page: Page, context: BrowserContext, env):
    ui_item = UI(page, context, user=env['user'], password=env['password'], url=env['url'])
    ui_item.page.goto(env['url'])
    return ui_item


@pytest.fixture(scope="session")
def env():
    config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    ".env")
    with open(config_file_path) as config:
        env_target = json.load(config)
    return env_target
