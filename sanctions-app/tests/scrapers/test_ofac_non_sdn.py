from scrapers.ofac_non_sdn import download_ofac_non_sdn

def test_download_ofac_non_sdn():
    result = download_ofac_non_sdn()
    
    assert isinstance(result, object)
    