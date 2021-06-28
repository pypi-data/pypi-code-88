# Copyright 2020 Karlsruhe Institute of Technology
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import json
from io import BytesIO

import qrcode
from flask_login import current_user

from .extras import is_nested_type
from .models import File
from .models import Record
from .models import RecordLink
from .schemas import FileSchema
from .schemas import RecordSchema
from kadi.ext.db import db
from kadi.lib.conversion import truncate
from kadi.lib.format import filesize
from kadi.lib.format import pretty_type_name
from kadi.lib.pdf import PDF
from kadi.lib.utils import parse_datetime_string
from kadi.lib.web import url_for
from kadi.modules.collections.models import Collection
from kadi.modules.permissions.core import get_permitted_objects


class RecordPDF(PDF):
    """Record PDF generation class.

    :param record: The record to generate a PDF from.
    :param user: (optional) The user to check for various access permissions when
        generating the PDF. Defaults to the current user.
    """

    def __init__(self, record, user=None):
        self.record = record
        self.user = user if user is not None else current_user

        super().__init__(title=self.record.title)

        self.render_header_section()
        self.render_basic_metadata()
        self.render_extras()
        self.render_files()
        self.render_record_links()
        self.render_collections()

    def render_header_section(self):
        """Render the header section of the record.

        The header sections contains the title, identifier and type of the record in the
        top left and a QR code pointing to the record in the top right, including a link
        pointing to the same location.
        """
        self.start_section("Overview")

        # Top right content.
        image_size = 20
        view_record_url = url_for("records.view_record", id=self.record.id)
        image = qrcode.make(view_record_url)
        cursor_x = self.get_x()
        cursor_y = self.get_y()
        start_x = self.w - self.r_margin - image_size

        self.image(
            image.get_image(),
            x=start_x,
            y=cursor_y,
            w=image_size,
            h=image_size,
            link=view_record_url,
        )
        self.rect(start_x, cursor_y, image_size, image_size)
        self.set_xy(start_x, cursor_y + image_size + 2)
        self.set_font(size=8)
        self.set_text_color(r=150, g=150, b=150)
        self.cell(w=image_size, txt=f"ID: {self.record.id}", align="C")
        self.set_text_color(r=0, g=0, b=0)
        self.set_xy(cursor_x, cursor_y)

        # Top left content.
        cell_width = self.epw * 0.85

        self.set_font(size=14, style="B")
        self.truncated_cell(cell_width, txt=self.record.title)
        self.ln(h=7)

        self.set_font(size=11)
        self.truncated_cell(cell_width, txt=f"@{self.record.identifier}")
        self.ln(h=11)

        self.set_font(style="B")
        self.truncated_cell(cell_width, txt=f"Type: {self.record.type or '-'}")
        self.ln(h=13)

    def render_basic_metadata(self):
        """Render the basic metadata of the record."""

        # Description.
        if self.record.description:
            self.set_font(family="DejaVuSansMono", size=11)
            self.write(txt=self.record.description)
            self.set_font(family="DejaVuSans")
        else:
            self.set_font(size=11, style="I")
            self.set_text_color(r=150, g=150, b=150)
            self.write(txt="No description.")
            self.set_text_color(r=0, g=0, b=0)

        self.ln(h=14)

        # Creator.
        displayname = self.record.creator.identity.displayname

        self.set_font()
        self.write(txt="Created by")
        self.set_font(style="B")
        self.write(txt=f" {displayname}")
        self.link(
            self.get_x() - self.get_string_width(displayname),
            self.get_y(),
            self.get_string_width(displayname),
            4,
            link=url_for("accounts.view_user", id=self.record.creator.id),
        )
        self.ln(h=7)

        # Creation date.
        self.set_font()
        self.write(txt=f"Created at {self.format_date(self.record.created_at)}")
        self.section(top=12, bottom=7)

        # License and tags.
        if self.record.license or self.record.tags.count() > 0:
            if self.record.license:
                title = self.record.license.title

                self.set_font(style="B")
                self.write(txt="License: ")
                self.set_font()
                self.write(txt=title)
                self.link(
                    self.get_x() - self.get_string_width(title),
                    self.get_y(),
                    self.get_string_width(title),
                    4,
                    link=self.record.license.url,
                )
                self.ln(h=5)

            if self.record.tags.count() > 0:
                if self.record.license:
                    self.ln(h=2)

                self.set_font(style="B")
                self.write(txt="Tags: ")
                self.set_font()
                self.write(txt="; ".join([tag.name for tag in self.record.tags]))
                self.ln(h=5)

            self.section(top=5, bottom=7)

    def render_extras(self):
        """Render the extra metadata of the record."""
        self.start_section("Extra metadata")

        self.set_font(size=11, style="B")
        self.write(h=5, txt="Extra metadata")
        self.ln(h=10)

        if self.record.extras:
            self.set_font(size=9)
            self.set_draw_color(r=200, g=200, b=200)
            self._render_extras(self.record.extras)
        else:
            self.set_font(style="I")
            self.set_text_color(r=150, g=150, b=150)
            self.write(h=5, txt="No extras.")
            self.set_text_color(r=0, g=0, b=0)
            self.ln(h=3)

        self.section(top=7, bottom=6)

    def _render_extras(self, extras, depth=0):
        for index, extra in enumerate(extras):
            if is_nested_type(extra["type"]):
                self._render_extra(index, extra, depth)
                self._render_extras(extra["value"], depth=depth + 1)
            else:
                self._render_extra(index, extra, depth)

        if depth == 0:
            self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())

    def _set_depth_color(self, depth):
        if depth % 2 == 1:
            self.set_fill_color(r=245, g=245, b=245)
        else:
            self.set_fill_color(r=256, g=256, b=256)

    def _render_extra(self, index, extra, depth):
        cell_height = 7
        nested_margin = 5
        column_width = (self.epw - nested_margin * depth) / 10

        # Render the "boxes" of the nested parent metadata entry, which automatically
        # gives us the correct left margin.
        for i in range(0, depth):
            self._set_depth_color(i)
            self.cell(w=nested_margin, h=cell_height, border="L", fill=True)

        self._set_depth_color(depth)

        if is_nested_type(extra["type"]):
            self.set_font(style="B")
            cell_width = column_width * 9
            key_border = "LT"
            type_border = "RT"
        else:
            cell_width = column_width * 5
            key_border = "LTB"
            type_border = "RTB"

        self.cell(
            w=cell_width,
            h=cell_height,
            border=key_border,
            fill=True,
            txt=self.truncate_string(extra.get("key", f"({index + 1})"), cell_width),
        )
        self.set_font()

        if not is_nested_type(extra["type"]):
            if extra["value"] is not None:
                if extra["type"] == "date":
                    date_time = parse_datetime_string(extra["value"])
                    value = self.format_date(date_time, include_micro=True)
                else:
                    value = str(extra["value"])
            else:
                self.set_font(style="I")
                value = "null"

            cell_width = column_width * 4
            if extra.get("unit"):
                cell_width = column_width * 3

            self.cell(
                w=cell_width,
                h=cell_height,
                border="TB",
                fill=True,
                txt=self.truncate_string(value, cell_width),
            )
            self.set_font()

            if extra.get("unit"):
                self.set_text_color(r=150, g=150, b=150)
                self.cell(
                    w=column_width,
                    h=cell_height,
                    border="TB",
                    fill=True,
                    txt=self.truncate_string(extra["unit"], cell_width),
                )

        self.set_text_color(r=150, g=150, b=150)
        self.cell(
            w=column_width,
            h=cell_height,
            border=type_border,
            fill=True,
            align="R",
            txt=pretty_type_name(extra["type"]).capitalize(),
        )
        self.set_text_color(r=0, g=0, b=0)
        self.ln(h=cell_height)

    def render_files(self):
        """Render the files of the record."""
        self.start_section("Files")

        self.set_font(size=11, style="B")
        self.write(h=5, txt="Files")
        self.ln(h=10)

        if self.record.active_files.count() > 0:
            for file in self.record.active_files.order_by(File.created_at):
                width = self.epw * 0.85

                self.set_font(size=11)
                self.cell(
                    w=width,
                    txt=self.truncate_string(file.name, width),
                    link=url_for(
                        "records.view_file", record_id=self.record.id, file_id=file.id
                    ),
                )
                self.set_font(size=9)
                self.set_text_color(r=150, g=150, b=150)
                self.cell(w=self.epw * 0.15, txt=filesize(file.size), align="R")
                self.set_text_color(r=0, g=0, b=0)
                self.ln(h=8)
        else:
            self.set_font(style="I")
            self.set_text_color(r=150, g=150, b=150)
            self.write(h=5, txt="No files.")
            self.set_text_color(r=0, g=0, b=0)
            self.ln(h=5)

        self.section(bottom=6)

    def render_record_links(self):
        """Render the links of the record with other records."""
        self.start_section("Record links")

        self.set_font(size=11, style="B")
        self.write(h=5, txt="Record links")
        self.ln(h=10)

        record_ids_query = (
            get_permitted_objects(self.user, "read", "record")
            .filter(Record.state == "active")
            .with_entities(Record.id)
        )
        record_links = RecordLink.query.filter(
            db.or_(
                db.and_(
                    RecordLink.record_from_id == self.record.id,
                    RecordLink.record_to_id.in_(record_ids_query),
                ),
                db.and_(
                    RecordLink.record_to_id == self.record.id,
                    RecordLink.record_from_id.in_(record_ids_query),
                ),
            )
        ).order_by(RecordLink.created_at)

        if record_links.count() > 0:
            for record_link in record_links:
                record_width = self.epw * 0.35
                link_width = self.epw * 0.3

                if record_link.record_from.id == self.record.id:
                    self.set_font(style="I")

                self.cell(
                    w=record_width,
                    txt=self.truncate_string(
                        f"@{record_link.record_from.identifier}", record_width
                    ),
                    link=url_for("records.view_record", id=record_link.record_from.id),
                )
                self.set_font(size=9)
                self.set_text_color(r=150, g=150, b=150)
                self.cell(
                    w=link_width,
                    txt=self.truncate_string(record_link.name, link_width),
                    align="C",
                )
                self.set_text_color(r=0, g=0, b=0)
                self.set_font(size=11)

                if record_link.record_to.id == self.record.id:
                    self.set_font(style="I")

                self.cell(
                    w=record_width,
                    txt=self.truncate_string(
                        f"@{record_link.record_to.identifier}", record_width
                    ),
                    link=url_for("records.view_record", id=record_link.record_to.id),
                    align="R",
                )
                self.set_font()
                self.ln(h=7)
        else:
            self.set_font(style="I")
            self.set_text_color(r=150, g=150, b=150)
            self.write(h=5, txt="No record links.")
            self.set_text_color(r=0, g=0, b=0)
            self.ln(h=5)

        self.section(top=5, bottom=6)

    def render_collections(self):
        """Render the collections the record is part of."""
        self.start_section("Collections")

        self.set_font(size=11, style="B")
        self.write(h=5, txt="Collections")
        self.ln(h=10)

        collection_ids_query = (
            get_permitted_objects(self.user, "read", "collection")
            .filter(Collection.state == "active")
            .with_entities(Collection.id)
        )
        collections = self.record.collections.filter(
            Collection.id.in_(collection_ids_query)
        ).order_by(Collection.last_modified.desc())

        if collections.count() > 0:
            self.set_font()

            for collection in collections:
                self.cell(
                    w=self.epw,
                    txt=self.truncate_string(f"@{collection.identifier}", self.epw),
                    link=url_for("collections.view_collection", id=collection.id),
                )
                self.ln(h=8)
        else:
            self.set_font(style="I")
            self.set_text_color(r=150, g=150, b=150)
            self.write(h=5, txt="No collections.")
            self.set_text_color(r=0, g=0, b=0)
            self.ln(h=5)


def get_export_data(record, export_type, user=None):
    """Export a record in a given format.

    :param record: The record to export.
    :param export_type: The export format, one of ``"dict"``, ``"json"`` ``"pdf"`` or
        ``"qr"``.
    :param user: (optional) The user to check for various access permissions when
        generating the export data. Defaults to the current user.
    :return: The exported record data, depending on the given export type, or ``None``
        if an unknown export type was given.
    """
    user = user if user is not None else current_user

    if export_type in ["dict", "json"]:
        exclude = ["_actions", "_links", "creator._actions", "creator._links"]

        schema = RecordSchema(exclude=exclude)
        data = schema.dump(record)

        schema = FileSchema(many=True, exclude=exclude)
        data["files"] = schema.dump(
            record.active_files.order_by(File.last_modified.desc())
        )

        if export_type == "json":
            return json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False)

        return data

    if export_type == "qr":
        image = qrcode.make(url_for("records.view_record", id=record.id))

        image_data = BytesIO()
        image.save(image_data, format="PNG")
        image_data.seek(0)

        return image_data

    if export_type == "pdf":
        pdf = RecordPDF(record, user=user)

        pdf_data = BytesIO()
        pdf.output(pdf_data)
        pdf_data.seek(0)

        return pdf_data

    return None


def _append_node(nodes, record):
    nodes.append(
        {
            "id": record.id,
            "identifier": truncate(record.identifier, 25),
            "identifier_full": record.identifier,
            "type": truncate(record.type, 15),
            "type_full": record.type,
            "url": url_for("records.view_record", id=record.id),
        }
    )


def _get_record_links(
    record_id, record_ids_query, nodes, links, processed_record_ids, added_record_ids
):
    new_record_ids = set()
    link_indices = {}
    link_lengths = {}

    # Limit the maximum amount of links per record to 100 for now.
    record_links = (
        RecordLink.query.filter(
            db.or_(
                db.and_(
                    RecordLink.record_from_id == record_id,
                    RecordLink.record_to_id.in_(record_ids_query),
                ),
                db.and_(
                    RecordLink.record_to_id == record_id,
                    RecordLink.record_from_id.in_(record_ids_query),
                ),
            )
        )
        .order_by(RecordLink.created_at)
        .limit(100)
    )

    for record_link in record_links:
        # Skip all links involving records that were already checked for their links.
        if (
            record_link.record_from_id in processed_record_ids
            or record_link.record_to_id in processed_record_ids
        ):
            continue

        source = record_link.record_from
        target = record_link.record_to

        for record in [source, target]:
            new_record_ids.add(record.id)

            if record.id not in added_record_ids:
                _append_node(nodes, record)
                added_record_ids.add(record.id)

        # The link indices are used to calculate the "curve" of a link when rendering
        # it. The index of a link is increased for each link that has the same source
        # and target, starting at 1.
        link_index = 1
        key = (source.id, target.id)

        if key in link_indices:
            link_indices[key] += 1
            link_index = link_indices[key]
        else:
            link_indices[key] = link_index

        # The link lengths are used to apply varying strengths of link forces to the
        # corresponding nodes based on the length of the (truncated) link name. Only the
        # largest length between each source and target record is taken, after all links
        # have been processed.
        link_name = truncate(record_link.name, 25)
        link_length = len(link_name)
        key = (
            (source.id, target.id) if source.id < target.id else (target.id, source.id)
        )

        if key in link_lengths:
            link_lengths[key] = max(link_length, link_lengths[key])
        else:
            link_lengths[key] = link_length

        links.append(
            {
                "source": source.id,
                "target": target.id,
                "name": link_name,
                "name_full": record_link.name,
                "link_index": link_index,
                "link_length": link_length,
            }
        )

    for link in links:
        key = (
            (link["source"], link["target"])
            if link["source"] < link["target"]
            else (link["target"], link["source"])
        )

        if key in link_lengths:
            link["link_length"] = link_lengths[key]

    processed_record_ids.add(record_id)
    return new_record_ids


def get_record_links_graph(record, depth=1, user=None):
    """Get all links of a record for visualizing them in a graph.

    Used in conjunction with "d3" to visualize all returned nodes and links in a force
    directed graph.

    :param record: The record to start with.
    :param depth: (optional) The link depth.
    :param user: (optional) The user to check for access permissions regarding the
        linked records. Defaults to the current user.
    :return: A dictionary containing the record links (``"links"``) as well as all
        records involved in the links (``"nodes"``).
    """
    user = user if user is not None else current_user

    record_ids_query = (
        get_permitted_objects(user, "read", "record")
        .filter(Record.state == "active")
        .with_entities(Record.id)
    )
    nodes = []
    links = []

    # Records to still check for their links.
    record_ids_to_process = {record.id}
    # Records already checked for their links.
    processed_record_ids = set()
    # Records already added to the node list.
    added_record_ids = set()

    # Add the start record itself to the nodes.
    _append_node(nodes, record)
    added_record_ids.add(record.id)

    for _ in range(0, depth):
        # Newly added records in the last iteration that are not processed yet.
        new_record_ids = set()

        for record_id in record_ids_to_process:
            new_record_ids |= _get_record_links(
                record_id,
                record_ids_query,
                nodes,
                links,
                processed_record_ids,
                added_record_ids,
            )

        record_ids_to_process = new_record_ids

    return {"nodes": nodes, "links": links}
