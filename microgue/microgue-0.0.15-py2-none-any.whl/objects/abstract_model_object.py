import uuid
from ..models.abstract_model import *
from .object import *


class RequiredAttributes(Exception):
    pass


class UniqueAttributes(Exception):
    pass


class AbstractModelObject(Object):
    """
    attributes: defined on Object

    protected_attributes: defined on Object

    default_attributes: defines the default values to use when inserting a new object in the database

    required_attributes: attributes that must be include when creating a new object in the database

    unique_attributes: attributes that must be unique across all entries in the database

    _model: the instantiated model that AbstractModelObject will use to connect to the database
    """
    default_attributes = {}
    required_attributes = []
    unique_attributes = []
    _model = None

    def __init__(self, attributes_or_pk_value={}, sk_value=None, *args, **kwargs):
        if type(attributes_or_pk_value) is dict:
            super().__init__(attributes_or_pk_value, *args, **kwargs)
        elif type(attributes_or_pk_value) is str:
            super().__init__(self._model.get(attributes_or_pk_value, sk_value), *args, **kwargs)

    @property
    def _pk(self):
        return self._model.pk

    @property
    def _pk_value(self):
        return self.__dict__.get(self._pk)

    @property
    def _sk(self):
        return self._model.sk

    @property
    def _sk_value(self):
        return  self.__dict__.get(self._sk)

    @classmethod
    def get_by_unique_attribute(cls, attribute, value):
        unique_key = "{}#{}".format(attribute.upper(), value)
        reference = cls._model.get(unique_key, '#UNIQUE')

        model_object = cls()
        model_object.deserialize(cls._model.get(reference.get('reference_pk'), reference.get('reference_sk')))

        return model_object

    def insert(self):
        # apply default values to missing attributes
        for key, value in self.default_attributes.items():
            if self.__dict__.get(key) is None:
                self.__setattr__(key, value)

        # enforce required attributes
        missing_required_attributes = self._get_missing_required_attributes()
        if missing_required_attributes:
            raise RequiredAttributes('missing the following required attributes: ' + ', '.join(missing_required_attributes))

        # enforce unique attributes
        if not self._pk_value:
            # provide a default pk value so the unique fields can reference it
            self.__setattr__(self._pk, str(uuid.uuid4()))

        # create a list of unique attributes to try and insert into the database
        insert_unique_attributes = []
        for attribute in self.unique_attributes:
            # check if the unique attribute has a value
            if self.__dict__.get(attribute):
                insert_unique_attributes.append(attribute)

        # attempt to insert all unique attributes
        self._insert_unique_attributes(insert_unique_attributes)

        try:
            # insert the object
            self.deserialize(self._model.insert(self.serialize(hide_protected_attributes=False)))
        except Exception as e:
            # undo all unique inserts if the object insert fails
            self._undo_insert_unique_attributes(insert_unique_attributes)
            raise e

    def update(self):
        # only pull the previous state of the object if necessary for checking uniqueness
        previous_state = None
        insert_unique_attributes = []

        # create a list of unique attributes to try and insert into the database
        for attribute in self.unique_attributes:
            # check if the unique attribute has a value
            attribute_value = self.__dict__.get(attribute)

            # pull the previous state of the object for checking if the unique attribute has changed
            if attribute_value and previous_state is None:
                previous_state = self._model.get(self._pk_value, self._sk_value)

            # only insert the new unique attribute if the value is different than in the previous state
            if attribute_value and attribute_value != previous_state.get(attribute):
                insert_unique_attributes.append(attribute)

        # attempt to insert all unique attributes
        self._insert_unique_attributes(insert_unique_attributes)

        try:
            # update the object
            self.deserialize(self._model.update(self.serialize(hide_protected_attributes=False)))
        except Exception as e:
            # undo all unique inserts if the object update fails
            self._undo_insert_unique_attributes(insert_unique_attributes)
            raise e
        else:
            # remove previous unique attribute values
            if previous_state:
                for old_attribute in insert_unique_attributes:
                    try:
                        self._model.delete("{}#{}".format(old_attribute.upper(), previous_state.get(old_attribute), "#UNIQUE"))
                    except:
                        pass

    def save(self):
        # check if the record exists
        if self._pk_value:
            try:
                record_exists = bool(self._model.get(self._pk_value, self._sk_value))
            except:
                record_exists = False

        # call update or insert accordingly
        if self._pk_value and record_exists:
            self.update()
        else:
            self.insert()

    def delete(self):
        # check if the object has unique attributes
        if self.unique_attributes:
            # undo all unique attributes before deleting the object
            user = self.__class__(self._pk_value, self._sk_value)
            user._undo_insert_unique_attributes(self.unique_attributes)

        # delete the object
        return self._model.delete(self._pk_value, self._sk_value)

    def _get_missing_required_attributes(self):
        missing_required_attributes = []
        for required_attribute in self.required_attributes:
            if self.__dict__.get(required_attribute) is None:
                missing_required_attributes.append(required_attribute)
        return missing_required_attributes

    def _insert_unique_attributes(self, unique_attributes):
        successes = []
        failures = []

        # attempt to insert each unique attribute as a special entry in the database ex EMAIL#test@test.com / #UNIQUE
        for attribute in unique_attributes:
            attribute_value = self.__dict__.get(attribute)

            unique_entry = {}
            unique_entry[self._pk] = "{}#{}".format(attribute.upper(), attribute_value)
            unique_entry['reference_pk'] = self._pk_value
            if self._sk:
                unique_entry[self._sk] = "#UNIQUE"
                unique_entry['reference_sk'] = self._sk_value

            try:
                # attempt to insert
                self._model.insert(unique_entry)
            except ItemAlreadyExists:
                # track failures
                failures.append(attribute)
            else:
                # track successes
                successes.append(attribute)

        # undo all success if any failures occurred
        if failures:
            self._undo_insert_unique_attributes(successes)
            raise UniqueAttributes("{} already exists".format(", ".join(failures)))

    def _undo_insert_unique_attributes(self, unique_attributes):
        for attribute in unique_attributes:
            try:
                delete_pk = "{}#{}".format(attribute.upper(), self.__dict__.get(attribute))
                delete_sk = "#UNIQUE"
                self._model.delete(delete_pk, delete_sk)
            except:
                pass
