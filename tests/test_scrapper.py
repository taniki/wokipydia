from wekeypedia.wikipedia_page import WikipediaPage

def test_fetch():
  page = WikipediaPage("unit testing")

  assert page.problem == None

def test_ambiguity():
  page = WikipediaPage("transformation")

  assert page.problem == "ambiguity"

def test_no_match():
  page = WikipediaPage("utin testgni")

  assert page.problem == "no match"

def test_links():
  page = WikipediaPage("unit testing")
  links = page.links()

  assert len(links) > 0

def test_direct_api():
  page = WikipediaPage()

  r = page.fetch_from_api_title("unit testing", opt_params={})

  print r

  assert "-1" not in r["query"]["pages"]

def test_direct_api_no_match():
  page = WikipediaPage()

  r = page.fetch_from_api_title("bleepbloopzerg", opt_params={})

  print r

  assert "-1" in r["query"]["pages"]