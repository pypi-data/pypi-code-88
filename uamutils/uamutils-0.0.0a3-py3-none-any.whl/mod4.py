import numpy as np
from datetime import datetime, timedelta

# TODO: more specific import
from .shared import *

class MOD4:
    '''
    Attributes:
        raw - np.array representing raw mod4 file data
        info - an instance of InfoRecord for self.raw
    '''

    def __init__(self, mod4_path):
        self.raw = None
        self.info = None

        raw = np.fromfile(mod4_path, dtype=np.float32)
        
        if not self._is_mod4(raw):
            raise ValueError(f'Given file ({mod4_path}) is not a valid mod4 file.')

        self.raw = raw
        self.info = InfoRecord(self.raw)

    def _is_mod4(self, raw_mod4):
        return raw_mod4[1020:1023].tobytes() == b'GLOBAL MODEL'

    def _take_n(self, start, count):
        return self.raw[start : start+count]

    def timestamp(self, dataset_id):
        start = self.info.timestamp_start_index(dataset_id)
        size = 6 # FIXME? check if it is specified in info record 
        raw_data = self._take_n(start, size)

        start_seconds, finish_seconds, days_dt, year = map(int, raw_data[:4])
        f10_7 = raw_data[4]

        year = datetime(year=year, month=1, day=1)
        days_dt = timedelta(days = days_dt - 1)
        start_secs_dt = timedelta(seconds=start_seconds)
        finish_secs_dt = timedelta(seconds=finish_seconds)

        started = year + days_dt + start_secs_dt
        finished = year + days_dt + finish_secs_dt
        f10_7 = round(f10_7, 1)

        return Timestamp(started, finished, f10_7)

    def dataset(self, dataset_id):
        '''
        Returns dataset (physical parameters data) for a given dataset_id as
        one-dimensional np.array with data layed out in Fortran order
        '''
        start = self.info.dataset_start_index(dataset_id)
        end = self.info.dataset_end_index(dataset_id)
        return self.raw[start : end+1]

    def altitudes(self, block_name):
        """
        TODO:
            - raise exception that given dataset doesn't have altitudes data
            - document exception here
        """
        if block_name == BlockName.sphere or block_name == BlockName.tube_to_sphere:
            start = self.info.sphere_altitudes_start_index
            count = self.info.sphere_altitudes_count
        else:
            return None

        return self._take_n(start, count).astype(float)

    def longitudes(self):
        # longitudes are shared for 'sphere' and 'potential' grids
        step = self.info.longitude_step
        count = int(360 / step)
        # ~? np.linspace(0.0, 355.0, num=lons_count)
        return np.array([step * i for i in range(count)])

    def colatitudes(self, block_name):
        """
        Extracts incomplete mod4 colatitudes,
        calculates the rest by using symmetry,
        returns the entire [0..180] colats array
        
        mod4 only stores colatitudes from (0, 90) open interval.
        
        TODO: raise and describe exception
        """

        if block_name == BlockName.sphere or block_name == BlockName.tube_to_sphere:
            start = self.info.sphere_colats_start_index
            count = self.info.sphere_colats_count
        elif block_name == BlockName.potential:
            start = self.info.potential_colats_start_index
            count = self.info.potential_colats_count
        else:
            return None  # TODO: raise exception that this dataset doesn't have colatitudes data

        # '- 3' is due to [0, 90, 180] missing in
        # both symmetrical open intervals
        incomplete_count = (count - 3) // 2
        incomplete_colats = self._take_n(start, incomplete_count)

        # don't include 90 here so it's not duplicated for the other half
        left_half = np.concatenate(([0], incomplete_colats))
        right_half = left_half + 90

        return np.concatenate((left_half, right_half, [180]))

    def tube_nodes(self):
        tubes_count = self.info.tubes_count
        nodes_count = self.info.tube_nodes_count
        nodes_split = self.info.tube_nodes_split

        start = self.info.tube_nodes_start
        # each node is a pair of (altitude, colatitude), hence *2
        nodes_1d = self._take_n(start, nodes_count * 2)
        
        #FIXME better way to do it?
        alts = np.array(nodes_1d[::2]) / 1e5
        colats = nodes_1d[1::2]
        # return list(zip(alts, nodes_1d[1::2]))
        nodes_raw = list(zip(alts, colats))

        nodes = []
        for tube_idx in range(tubes_count):
            node_start = sum(nodes_split[:tube_idx])
            for point_idx in range(nodes_split[tube_idx]):
                node_idx = node_start + point_idx
                alt, colat = nodes_raw[node_idx]   

                nodes.append({
                        'tube': tube_idx,
                        'node': node_idx,
                        'local_offset': point_idx,
                        'alt': alt,
                        'colat': colat,
                        'node_local': point_idx
                        })

        return nodes, nodes_raw

    # def tube_nodes_mapping(self):
    #     nodes_split = self.info.tube_nodes_split
    #     tubes_count = self.info.tubes_count

    #     # mapping = [{} for x in range(140)]
    #     mapping = [{} for x in range(tubes_count)]

    #     nodes_flat = iter(tube_nodes(mod4))

    #     for tube_idx in range(tubes_count):
    #         for point_idx in range(nodes_split[tube_idx]):
    #             alt, colat = next(nodes_flat)
    #             alt /= 1e5

    #             mapping[tube_idx][point_idx] = (alt, colat)

    #             # nodes_1d.append((alt, colat))
    #     return mapping


# TODO: rename fields - use constants defined by UAM 
    # _may be_ add alises? (it's hard to establish new names)
class InfoRecord:
    '''
    Contains:
    1) essential data from information record of a given mod4 file
    2) helper methods for working with it
    This class looks up all the internal info record indices to
    return location of the actual data like coordinate grids of
    physical parameters).
    '''
    def __init__(self, mod4_raw):

        # TODO: look up the actual value in info_record
        self.record_size = 1024

        info = mod4_raw[:self.record_size]

        self.storage_place_indices = (info[0:17] - 1).astype(int)
        self.storage_place_offsets = info[37:57].astype(int)
        self.storage_place_lenghts = info[57:77].astype(int)

        # ~? create namespaces for all these stuff to access like info.sphere.altitudes_count

        self.tube_fieldlines_count = int(info[99])

        # tube fieldlines count is the count of potential's incomplete colats
        self.potential_colats_start_index = 300
        self.potential_colats_count = int(3 + 2*self.tube_fieldlines_count)

        self.longitude_step = info[83]

        # make sphere, tube (and potential?) into named tuples
        # so that data is accesed like info.sphere.altitudes_count
        self.sphere_altitudes_start_index = 500
        self.sphere_altitudes_count = int(info[89])
        self.sphere_colats_start_index = 400
        self.sphere_colats_count = int(info[105])

        # tube_node named tuple? (alt, colat)
        self.tube_nodes_count = int(info[100])
        # TODO: do that with dataset_start or something
        self.tube_nodes_start = self.record_size  # 2nd dataset
        self.tubes_count = int(info[99])
        # count of nodes for each tube
        self.tube_nodes_split = info[110 : 110 + self.tubes_count].astype(int)

#         self.tube_params_count =
#         self.sphere_params_count =

        self.info = info

    def timestamp_start_index(self, dataset_id):
        block_name = dataset_id.block_name
        # record_local_index - index of the record in which the time label begins (counting from storage place offset)
        # start_local_index - index of timestamp's starting number (counting from record defined by record local index)
        # ~TODO: refactor this mess
        if block_name == BlockName.potential:
            record_local_index, start_local_index = map(int, self.info.take([103, 104]) - 1)
        elif block_name == BlockName.sphere:
            record_local_index, start_local_index = map(int, self.info.take([96, 98]) - 1)
        elif block_name == BlockName.tube:
            record_local_index, start_local_index = map(int, self.info.take([95, 97]) - 1)
        elif block_name == BlockName.tube_to_sphere:
            record_local_index, start_local_index = map(int, self.info.take([106, 107]) - 1)
        else:
            Error('No such block name exists.')

        offset = self._storage_place_offset(dataset_id)

        return self.record_size * (offset + record_local_index) + start_local_index

    def dataset_start_index(self, dataset_id):
        return self._storage_place_offset(dataset_id) * self.record_size

    def dataset_end_index(self, dataset_id):
        return self.timestamp_start_index(dataset_id) - 1

    def _storage_place_index(self, dataset_id):
        dataset_idx = self._dataset_index(dataset_id)
        return int(self.storage_place_indices[dataset_idx])

    def _storage_place_offset(self, dataset):
        idx = self._storage_place_index(dataset)
        return int(self.storage_place_offsets[idx])

    def _storage_place_length(self, dataset):
        idx = self._storage_place_index(dataset)
        return int(self.storage_place_lenghts[idx])

    # ~TODO: change the name of this method to something like dataset_info_index 
    #   (otherwise it collides with self.dataset_start_index, although they are very different!)
    def _dataset_index(self, dataset):
        mapping = {
            DatasetID(BlockName.potential, TimeMoment.current): 14,
            DatasetID(BlockName.sphere, TimeMoment.current): 4,
            DatasetID(BlockName.tube, TimeMoment.current): 5,
            DatasetID(BlockName.tube_to_sphere, TimeMoment.current): 6
        }

        return mapping[dataset]
