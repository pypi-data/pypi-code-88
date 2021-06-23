import os
import gazu
import re

from kabaret import flow
from kabaret.flow_contextual_dict import ContextualView, get_contextual_dict

from .departments import Department
from .maputils import ItemMap, CreateItemAction, ClearMapAction
from .lib import AssetDependency, DropAssetAction  # , KitsuSettingsView
from .kitsu import KitsuSequence, KitsuShot, UpdateItemsKitsuSettings
from .site import RequestRevisionsAs
from .dependency import get_dependencies


class Casting(flow.Map):

    ICON = ("icons.flow", "casting")

    drag_assets = flow.Child(DropAssetAction)

    @classmethod
    def mapped_type(cls):
        return AssetDependency

    def columns(self):
        return ["Name", "Description"]

    def row(self, item):
        _, row = super(Casting, self).row(item)

        return item.get().oid(), row

    def _fill_row_cells(self, row, item):
        asset = item.get()
        row["Name"] = asset.id.get()
        row["Description"] = asset.description.get()


class DisplayKitsuSettings(flow.Action):

    _map = flow.Parent()

    def needs_dialog(self):
        return False

    def allow_context(self, context):
        return context and context.endswith(".inline")

    def run(self, button):
        displayed = self._map._display_kitsu_settings.get()
        self._map._display_kitsu_settings.set(not displayed)
        self._map.touch()


class ShotDepartments(flow.Object):

    layout = flow.Child(Department).ui(expanded=True)
    animation = flow.Child(Department).ui(expanded=True)
    compositing = flow.Child(Department).ui(expanded=True)


class ShotElements(flow.values.MultiChoiceValue):
    
    def choices(self):
        template = self.root().project().admin.dependency_templates['shot']
        return list(template.get_dependencies().keys())


class RequestShot(RequestRevisionsAs):
    
    _shot = flow.Parent()
    _sequence = flow.Parent(3)
    elements = flow.Param([], ShotElements).watched().ui(
        label="Elements to request"
    )
    select_all = flow.SessionParam(False).watched().ui(editor='bool')
    last_only = flow.SessionParam(True).watched().ui(hidden=True)
    predictive_only = flow.SessionParam(False).ui(
        editor='bool',
        tooltip='Include predictive dependencies only'
    )
    latest = flow.SessionParam(True).ui(
        editor='bool',
        label='Latest published work',
        editable=False,
        hidden=True,
    )
    pattern = flow.SessionParam("").watched().ui(
        placeholder="Revision oid pattern(s)",
        hidden=True,
    )
    revision_oids = flow.SessionParam("").ui(
        editor="textarea",
        html=True,
        editable=False,
    )
    
    def _title(self):
        seq_num = re.findall(r'\d+', self._sequence.name())[0]
        shot_num = re.findall(r'\d+', self._shot.name())[0]
        return f"Request sq{seq_num}sc{shot_num}"
    
    def _get_casting(self):
        bindings = self.root().project().kitsu_bindings()
        casting = bindings.get_shot_casting(
            self._shot.name(),
            self._sequence.name()
        )

        return casting
    
    def get_buttons(self):
        self.message.set("<h2>%s</h2>" % self._title())
        self._kitsu_casting = self._get_casting()
        
        return ['Request', 'Refresh revision oids', 'Close']
    
    def _get_revision_oids(self, root_oid, file_name, file_data):
        file_oid = "%s/departments/%s/files/%s" % (
            root_oid,
            file_data['department'],
            file_name.replace('.', '_')
        )
        rev_name_pattern = file_data.get('revision', '[last]')
        
        rev_oids = ["%s/history/revisions/%s" % (
            file_oid,
            rev_name_pattern,
        )]
        
        needs_deps = file_data.get('needs_deps', False)
        
        # Get file dependencies if needed
        if not needs_deps:
            return rev_oids
        
        if rev_name_pattern == '[last]':
            rev_name = None
        else:
            rev_name = rev_name_pattern
        
        if not self.root().session().cmds.Flow.exists(file_oid):
            print("ERROR: File %s not defined in the flow" % file_oid)
            return rev_oids
        
        file_object = self.root().get_object(file_oid)
        file_deps = get_dependencies(
            file_object,
            predictive=True,
            real=not self.predictive_only.get(),
            revision_name=rev_name
        )
        
        for dep in file_deps:
            if dep['in_breakdown']:
                rev_oid = dep['revision_oid']
                if rev_oid is not None:
                    rev_oids.append(rev_oid)
                else:
                    print((
                        "WARNING: dependency %s in breakdown "
                        "but not defined in the flow" % dep['entity_oid']
                    ))
        
        return rev_oids
    
    def child_value_changed(self, child_value):
        if child_value is self.select_all:
            if self.select_all.get():
                self.elements.set(self.elements.choices())
            else:
                self.elements.set([])
        else:
            super(RequestShot, self).child_value_changed(child_value)
    
    def run(self, button):
        if button == 'Close':
            return
        
        elements = self.elements.get()
        template = self.root().project().admin.dependency_templates['shot']
        bindings = self.root().project().kitsu_bindings()
        deps = template.get_dependencies()
        
        oids = set()
        
        for element in self.elements.get():
            dep_data = deps[element]
            kitsu_data = dep_data.get('kitsu', None)
            
            if kitsu_data is not None:
                # Kitsu dependencies
                if kitsu_data['entity'] == 'Asset':
                    for asset_name, asset_data in self._kitsu_casting.items():
                        asset_type = asset_data['type']
                        
                        if asset_type != kitsu_data['type']:
                            continue
                        
                        files_data = template.get_dependency_files(element)
                        asset_oid = bindings.get_asset_oid(asset_name)
                        
                        # Get files
                        for file_name, file_data in files_data.items():
                            rev_oids = self._get_revision_oids(asset_oid, file_name, file_data)
                            # pprint(oids)
                            oids = oids.union(set(rev_oids))
            else:
                # Default dependencies
                files_data = template.get_dependency_files(element)
                
                for file_name, file_data in files_data.items():
                    rev_oids = self._get_revision_oids(self._shot.oid(), file_name, file_data)
                    oids = oids.union(set(rev_oids))
        
        oids = sorted(list(oids))
        
        if button == 'Refresh revision oids':
            self.pattern.set(';'.join(oids))
            return self.get_result(close=False)
        
        return super(RequestShot, self).run(button)


class Shot(KitsuShot):

    ICON = ("icons.flow", "shot")

    _sequence = flow.Parent(2)
    request = flow.Child(RequestShot)
    settings = flow.Child(ContextualView).ui(hidden=True)
    # casting = flow.Child(Casting)

    description = flow.Param("")
    departments = flow.Child(ShotDepartments).ui(expanded=True)

    def get_default_contextual_edits(self, context_name):
        if context_name == "settings":
            return dict(shot=self.name())


class Shots(ItemMap):

    ICON = ("icons.flow", "shot")

    item_prefix = "p"

    _display_kitsu_settings = flow.BoolParam(False)

    with flow.group("Kitsu"):
        toggle_kitsu_settings = flow.Child(DisplayKitsuSettings)
        update_kitsu_settings = flow.Child(UpdateItemsKitsuSettings)

    @classmethod
    def mapped_type(cls):
        return flow.injection.injectable(Shot)

    def columns(self):
        names = ["Name"]

        if self._display_kitsu_settings.get():
            names.extend(
                ["Movement", "Nb frames", "Frame in", "Frame out", "Multiplan"]
            )

        return names

    def _fill_row_cells(self, row, item):
        row["Name"] = item.name()

        if self._display_kitsu_settings.get():
            row["Nb frames"] = item.kitsu_settings["nb_frames"].get()

            data = item.kitsu_settings["data"].get()

            row["Movement"] = data["movement"]
            row["Frame in"] = data["frame_in"]
            row["Frame out"] = data["frame_out"]
            row["Multiplan"] = data["multiplan"]


class SequenceElements(flow.values.MultiChoiceValue):

    CHOICES = [
        'Sets',
        'Characters',
        'Props',
        'Audios',
        'Storyboards',
        'Layout scenes'
    ]


class RequestSequence(RequestRevisionsAs):

    _sequence = flow.Parent()
    film = flow.Param("siren").ui(editable=False)
    elements = flow.Param([], SequenceElements).watched().ui(
        label="Elements to request"
    )
    select_all = flow.SessionParam(False).watched().ui(editor='bool')
    last_only = flow.SessionParam(True).watched().ui(editor='bool')
    latest = flow.SessionParam(True).ui(
        editor='bool',
        label='Latest published work',
        editable=False,
        hidden=True,
    )
    pattern = flow.SessionParam("").watched().ui(
        placeholder="Revision oid pattern(s)",
        hidden=True,
    )
    revision_oids = flow.SessionParam("").ui(
        editor="textarea",
        html=True,
        editable=False,
    )

    def _asset_type_short_name(self, kitsu_name):
        short_names = {
            'Characters': 'chars',
            'Props': 'props',
            'Sets': 'sets',
        }

        return short_names[kitsu_name]

    def _oid_patterns(self, element_name):
        project_name = self.root().project().name()
        asset_oid_root = "/"+project_name+"/asset_lib/asset_types/{asset_type}/asset_families/{asset_family}/assets/{asset_name}/departments"
        set_oid_root = "/"+project_name+"/asset_lib/asset_types/sets/asset_families/"+self._sequence.name()+"/assets/*/departments"
        shot_oid_root = "/"+project_name+"/films/"+self.film.get()+"/sequences/"+self._sequence.name()+"/shots/*/departments"

        oids_by_element = {
            'Sets': [set_oid_root+"/design/files/layers"],
            'Characters': [
                asset_oid_root+"/modeling/files/modelisation_export_fbx",
                asset_oid_root+"/rigging/files/rig_ok_blend",
                asset_oid_root+"/shading/files/textures",
            ],
            'Props': [
                asset_oid_root+"/modeling/files/modelisation_export_fbx",
                asset_oid_root+"/rigging/files/rig_ok_blend",
                asset_oid_root+"/shading/files/textures",
            ],
            'Audios': [shot_oid_root+"/misc/files/audio_wav"],
            'Storyboards': [shot_oid_root+"/misc/files/board_mp4"],
            'Layout scenes': [shot_oid_root+"/layout/files/layout_blend"]
        }

        return oids_by_element[element_name]
    
    def get_casting(self):
        kitsu_api = self.root().project().kitsu_api()
        sequence_casting = kitsu_api.get_sequence_casting(
            kitsu_api.get_sequence_data(self._sequence.name())
        )
        casting = dict()
        
        for shot_casting in list(sequence_casting.values()):
            for asset in shot_casting:
                asset_id = asset['asset_id']
                asset_name = asset['asset_name']

                casting[asset_id] = dict(
                    asset_name=asset_name,
                    asset_type=self._asset_type_short_name(asset['asset_type_name']),
                    asset_family=kitsu_api.get_asset_data(asset_name)['data']['family']
                )
        
        return casting
    
    def get_asset_file_oids(self, element_name):
        if not element_name in ['Props', 'Characters']:
            oids = self._oid_patterns(element_name)
        else:
            oids = []
            assets = [asset for asset in list(self._sequence_casting.values()) if asset['asset_type'] == self._asset_type_short_name(element_name)]

            for asset in assets:
                for pattern in self._oid_patterns(element_name):
                    oids.append(pattern.format(**asset))
        
        if self.last_only.get():
            revision_pattern = "[last]"
        else:
            revision_pattern = "v???"

        oids = [oid+f"/history/revisions/{revision_pattern}" for oid in oids]

        return oids
    
    def _title(self):
        return "Request sequence %s" % re.findall(r'\d+', self._sequence.name())[0]
    
    def _revert_to_defaults(self):
        self.elements.revert_to_default()
        self.select_all.revert_to_default()
        self.last_only.revert_to_default()

    def child_value_changed(self, child_value):
        if child_value is self.select_all:
            if self.select_all.get():
                self.elements.set(SequenceElements.CHOICES)
            else:
                self.elements.set([])
        elif child_value is self.last_only:
            self.elements.notify()
        elif child_value is self.elements:
            patterns = []
            for element in self.elements.get():
                patterns += self.get_asset_file_oids(element)
            
            self.pattern.set(';'.join(patterns))
        else:
            super(RequestSequence, self).child_value_changed(child_value)
    
    def get_buttons(self):
        self.message.set("<h2>%s</h2>" % self._title())
        self._revert_to_defaults()

        # Cache Kitsu sequence casting
        if not hasattr(self, '_sequence_casting') or not self._sequence_casting:
            self._sequence_casting = self.get_casting()

        return ['Request', 'Close']


class Sequence(KitsuSequence):

    ICON = ("icons.flow", "sequence")

    _map = flow.Parent()

    settings = flow.Child(ContextualView).ui(hidden=True)
    description = flow.Param("")
    shots = flow.Child(Shots).ui(expanded=True)
    request = flow.Child(RequestSequence).ui(hidden=True)

    def get_default_contextual_edits(self, context_name):
        if context_name == "settings":
            return dict(sequence=self.name())


class ClearSequencesAction(ClearMapAction):
    def run(self, button):
        for sequence in self._map.mapped_items():
            for shot in sequence.shots.mapped_items():
                shot.kitsu_settings.clear()

            sequence.shots.clear()
            sequence.kitsu_settings.clear()

        super(ClearSequencesAction, self).run(button)


class Sequences(ItemMap):

    ICON = ("icons.flow", "sequence")

    item_prefix = "s"

    create_sequence = flow.Child(CreateItemAction)
    update_kitsu_settings = flow.Child(UpdateItemsKitsuSettings)

    @classmethod
    def mapped_type(cls):
        return Sequence

    def columns(self):
        return ["Name"]

    def _fill_row_cells(self, row, item):
        row["Name"] = item.name()

    def get_default_contextual_edits(self, context_name):
        if context_name == "settings":
            return dict(file_category="PROD")
