import taipy as tp
from taipy.gui import Gui

from taipy import Rest
from pages import *


pages = {
    "/": root_page,
    "explanation": explanation,
    "data_vis": data_vis,
	"prediction": prediction
}


if __name__ == "__main__":
    rest = Rest()

    gui = Gui(pages=pages)
    tp.run(gui, rest, title="Football Ads Statistics Simulator", run_browser=False, debug=True)
