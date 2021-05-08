import pytest
from myapp.main import read_root, read_item

@pytest.mark.asyncio
async def test_read_item():
    result = await read_item(42)
    assert result == {"item_id": 42, "q": None}