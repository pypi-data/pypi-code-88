from ._classifier import OCLRandomForestClassifier
import numpy as np

class OCLRandomForestLabelClassifier():
    def __init__(self, opencl_filename="temp.cl", max_depth: int = 2, num_ensembles: int = 10):
        """
        A RandomForestClassifier for label classification that converts itself to OpenCL after training.

        Parameters
        ----------
        opencl_filename : str (optional)
        max_depth : int (optional)
        num_ensembles : int (optional)

        See Also
        --------
            https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
        """
        self.FEATURE_SPECIFICATION_KEY = "feature_specification = "

        self.classifier = OCLRandomForestClassifier(opencl_filename=opencl_filename, max_depth=max_depth,
                                                    num_ensembles=num_ensembles)

        self.classifier.feature_specification = self.classifier._get_feature_specification_from_opencl_file(opencl_filename)

    def train(self, features: str, labels, sparse_annotation, image=None):
        """
        Train a classifier that can differentiate label types according to intensity, size and shape.

        Parameters
        ----------
        features: Comma separated string containing those:
            'area',
            'min_intensity', 'max_intensity', 'sum_intensity', 'mean_intensity', 'standard_deviation_intensity',
            'mass_center_x', 'mass_center_y', 'mass_center_z',
            'centroid_x', 'centroid_y', 'centroid_z',
            'max_distance_to_centroid', 'max_distance_to_mass_center',
            'mean_max_distance_to_centroid_ratio', 'mean_max_distance_to_mass_center_ratio'
        labels: label image
        sparse_annotation: label image with annotations. If one label is annotated with multiple classes, the
            maximimum is considered while training.
        image: intensity image (optional)

        """
        selected_features, gt = self._make_features(features, labels, sparse_annotation, image)

        self.classifier.feature_specification = features
        self.classifier.train(selected_features, gt)

    def predict(self, labels, image=None):
        """

        Parameters
        ----------
        labels: label image
        image: intensity image

        Returns
        -------
        label image representing a semantic segmentation: pixel intensities represent label class

        """
        selected_features, gt = self._make_features(self.classifier.feature_specification, labels, None, image)

        import pyclesperanto_prototype as cle

        output = cle.create(selected_features[0].shape)
        parameters = {}
        for i, f in enumerate(selected_features):
            parameters['in' + str(i)] = cle.push(f)

        parameters['out'] = output

        cle.execute(None, self.classifier.opencl_file, "predict", selected_features[0].shape, parameters)

        # set background to zero
        cle.set_column(output, 0, 0)

        result_labels = cle.create_labels_like(labels)
        cle.replace_intensities(labels, output, result_labels)

        return result_labels

    def _make_features(self, features: str, labels, annotation=None, image=None):

        import pyclesperanto_prototype as cle
        pixel_statistics = cle.statistics_of_background_and_labelled_pixels(image, labels)

        # determine ground truth
        annotation_statistics = cle.statistics_of_background_and_labelled_pixels(annotation, labels)
        classification_gt = annotation_statistics['max_intensity']

        table, gt = self._select_features(annotation_statistics, features.split(','), classification_gt)

        return table, gt

    def _select_features(self, all_features, features_to_select, ground_truth=None):

        result = []
        if ground_truth is not None:
            mask = ground_truth > 0
            for key in features_to_select:
                result.append(np.asarray([all_features[key][mask]]))

            return result, ground_truth[mask]
        else:
            for key in features_to_select:
                result.append(np.asarray([all_features[key]]))
            return result, None
