from brando.reporter import generate_validation_urls


def test_generate_validation_urls():
    urls = generate_validation_urls("Aeroaera")
    assert "Aeroaera" in urls["google"]
    assert "Aeroaera" in urls["uspto"]
    assert "Aeroaera" in urls["wipo"]
    assert "Aeroaera" in urls["urban_dictionary"]

    # Check escaped URL parameter encoding
    spaced_urls = generate_validation_urls("Aero Aera")
    google_url = spaced_urls["google"]
    assert "Aero+Aera" in google_url or "Aero%20Aera" in google_url
