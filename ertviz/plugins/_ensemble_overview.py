import dash_html_components as html
from webviz_config import WebvizPluginABC
from ertviz.views import ensemble_selector_view
from ertviz.controllers import ensemble_selector_controller


class EnsembleOverview(WebvizPluginABC):
    def __init__(self, app, project_identifier: str):
        super().__init__()
        self.project_identifier = project_identifier
        self.ensembles = {}
        self.set_callbacks(app)

    @property
    def layout(self):
        return html.Div(
            [
                html.P(
                    "Webvis-ERT a visualization tool for ensembles-output generated by ERT."
                ),
                html.Div(children=ensemble_selector_view(self)),
            ]
        )

    def set_callbacks(self, app):
        ensemble_selector_controller(self, app)
        pass
