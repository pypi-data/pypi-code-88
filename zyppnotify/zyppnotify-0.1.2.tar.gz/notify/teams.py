import pymsteams


class NotifyTeams:
    def __init__(self, webhook: str):
        """

        Parameters
        ----------
        webhook: str
            url for sending the teams message
        """

        self.msg = pymsteams.connectorcard(webhook)
        self.msg.color("#F0B62E")

    def create_dataframe_report(self, dfs: dict) -> None:
        """

        Parameters
        ----------

        dfs: dict
            Dataframes containing {name, df} as key value pairs

        Returns
        -------
        None
            Adds a section for the table to the teams message object.

        """
        for df_name, df in dfs.items():
            section = pymsteams.cardsection()
            section.activityTitle(f"<h1><b>{df_name}</b></h1>")
            section.activityImage(
                "https://www.vhv.rs/dpng/d/"
                "593-5938489_table-icon-circle-png-png-download-table-icon.png"
            )
            section.text(
                f"> In totaal **{df.shape[0]}** records met **{df.shape[1]}** kolommen verwerkt"
            )
            self.msg.addSection(section)

    def create_buttons(self, buttons: dict) -> None:
        """

        Parameters
        ----------
        buttons: dict
            dictionairy containing button_name, button_link as key, value pairs.

        Returns
        -------
        None
            Adds the button(s) to the teams message

        """

        for button_name, button_link in buttons.items():
            self.msg.addLinkButton(button_name, button_link)

    def basic_message(
        self,
        title: str,
        message: str = None,
        buttons: dict = None,
        dfs: dict = None,
    ) -> None:
        """
        This function posts a message, containing a section, in a Microsoft Teams channel

        Parameters
        ----------
        dfs: dict
            Dataframes dictionary, with keys as dataframe name and value as dataframe.
        title: str
            Title of the message (optional)
        message: str
            Content of the message (optional)
        buttons: dict
            dictionary of button_name, button_url as key value pairs

        Returns
        -------
        None
            sends a message in a teams channel, reporting col en records as information.
        """

        self.msg.title(title)  # always required.

        if message:
            self.msg.text(message)

        if dfs:
            self.create_dataframe_report(dfs)

        if buttons:
            self.create_buttons(buttons)

        self.msg.send()
