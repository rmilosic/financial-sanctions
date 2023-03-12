from scrapers.ofac_sdn import download_ofac_sdn

def test_download_ofac_sdn():
    result = download_ofac_sdn()
    
    assert isinstance(result, object)
    