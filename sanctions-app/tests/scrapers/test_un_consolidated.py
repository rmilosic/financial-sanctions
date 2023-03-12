from scrapers.un_sc_consolidated_list import download_un_consolidated

def test_download_un_consolidated():
    result = download_un_consolidated()
    
    assert isinstance(result, object)
    