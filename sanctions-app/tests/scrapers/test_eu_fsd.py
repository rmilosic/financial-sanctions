from scrapers.eu_fsd import download_eu_fsd

def test_download_eu_fsd():
    result = download_eu_fsd()
    
    assert isinstance(result, object)
    