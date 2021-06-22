# Copyright 2018-2021 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Contains the parameter shift transforms for qubit systems.
"""
import pennylane as qml


def parameter_shift_gradient(tape, idx, gradient_recipe=None):
    r"""Generate the tapes and postprocessing methods required to compute the gradient of a
    parameter on a quantum tape using the parameter-shift method.

    Args:
        tape (~.QuantumTape): the tape to differentiate
        idx (int): trainable parameter index to differentiate with respect to
        gradient_recipe tuple(Union(list[list[float]], None)) or None: Gradient recipe for the
            parameter-shift method.

            This is a tuple with one nested list per operation parameter. For
            parameter :math:`\phi_k`, the nested list contains elements of the form
            :math:`[c_i, a_i, s_i]` where :math:`i` is the index of the
            term, resulting in a gradient recipe of

            .. math:: \frac{\partial}{\partial\phi_k}f = \sum_{i} c_i f(a_i \phi_k + s_i).

            If ``None``, the default gradient recipe containing the two terms
            :math:`[c_0, a_0, s_0]=[1/2, 1, \pi/2]` and :math:`[c_1, a_1,
            s_1]=[-1/2, 1, -\pi/2]` is assumed for every parameter.

    Returns:
        tuple[list[QuantumTape], function]: A tuple containing the list of generated tapes,
        in addition to a post-processing function to be applied to the evaluated
        tapes.
    """
    t_idx = list(tape.trainable_params)[idx]
    op = tape._par_info[t_idx]["op"]
    p_idx = tape._par_info[t_idx]["p_idx"]

    if gradient_recipe is None:
        gradient_recipe = op.get_parameter_shift(p_idx, shift=np.pi / 2)

    shift = np.zeros_like(params)
    coeffs = []
    tapes = []

    for c, a, s in gradient_recipe:
        shift[idx] = s
        shifted_tape = tape.copy(copy_operations=True)
        shifted_tape.set_parameters(a * params + shift)

        coeffs.append(c)
        tapes.append(shifted_tape)

    def processing_fn(results):
        """Computes the gradient of the parameter at index idx via the
        parameter-shift method.

        Args:
            results (list[real]): evaluated quantum tapes

        Returns:
            array[float]: 1-dimensional array of length determined by the tape output
            measurement statistics
        """
        results = qml.math.squeeze(results)
        return sum([c * r for c, r in zip(coeffs, results)])

    return tapes, processing_fn


def _get_variance_idx(tape):
    """Returns the locations of any variance measurements in the
    measurement queue of a tape.

    Args:
        tape (~.QuantumTape): the input tape

    Returns:
        tuple(array[int], array[bool]): Returns a tuple that contains the indices in the
        measurement queue that correspond to variances, as well as a mask.
    """
    var_mask = [m.return_type is qml.operation.Variance for m in tape.measurements]

    if not any(var_mask):
        return None

    return np.where(var_mask)[0], var_mask


def _var_to_expectation(tape):
    var_idx, var_mask = _get_variance_idx(tape)

    # Get <A>, the expectation value of the tape with unshifted parameters.
    unshifted_ev_tape = tape.copy()

    # Convert all variance measurements on the tape into expectation values
    for i in var_idx:
        obs = unshifted_ev_tape._measurements[i].obs
        unshifted_ev_tape._measurements[i] = qml.measure.MeasurementProcess(
            qml.operation.Expectation, obs=obs
        )

    return unshifted_ev_tape


def parameter_shift_gradient_var(tape, idx, gradient_recipe=None, expectation=None):
    r"""Generate the tapes and postprocessing methods required to compute the gradient of a
    parameter on a quantum tape that ends with a variance measurement.

    Args:
        idx (int): trainable parameter index to differentiate with respect to
        gradient_recipe tuple(Union(list[list[float]], None)) or None: Gradient recipe for the
            parameter-shift method.

            This is a tuple with one nested list per operation parameter. For
            parameter :math:`\phi_k`, the nested list contains elements of the form
            :math:`[c_i, a_i, s_i]` where :math:`i` is the index of the
            term, resulting in a gradient recipe of

            .. math:: \frac{\partial}{\partial\phi_k}f = \sum_{i} c_i f(a_i \phi_k + s_i).

            If ``None``, the default gradient recipe containing the two terms
            :math:`[c_0, a_0, s_0]=[1/2, 1, \pi/2]` and :math:`[c_1, a_1,
            s_1]=[-1/2, 1, -\pi/2]` is assumed for every parameter.
        expectation (array[float]): The output value of the executed tape with all variances
            converted into expectation values. If not provided, this is computed
            automatically.

    Returns:
        tuple[list[QuantumTape], function]: A tuple containing the list of generated tapes,
        in addition to a post-processing function to be applied to the evaluated
        tapes.
    """
    tapes = []
    var_idx, var_mask = _get_variance_idx(tape)
    unshifted_ev_tape = _var_to_expectation(tape)

    # evaluate the analytic derivative of <A>
    gradient_tapes, grad_fn = parameter_shift_gradient(
        unshifted_ev_tape, idx, gradient_recipe=gradient_recipe
    )
    tapes.extend(gradient_tapes)

    # For involutory observables (A^2 = I) we have d<A^2>/dp = 0.
    # Currently, the only observable we have in PL that may be non-involutory is qml.Hermitian
    involutory = [i for i in var_idx if tape.observables[i].name != "Hermitian"]

    # If there are non-involutory observables A present, we must compute d<A^2>/dp.
    non_involutory = set(var_idx) - set(involutory)

    if non_involutory:
        gradient_sq_tapes = tape.copy()

        for i in non_involutory:
            # We need to calculate d<A^2>/dp; to do so, we replace the
            # involutory observables A in the queue with A^2.
            obs = pdA2_tape._measurements[i].obs
            A = obs.matrix

            obs = qml.transforms.invisible(qml.Hermitian)(A @ A, wires=obs.wires)
            pdA2_tape._measurements[i] = MeasurementProcess(qml.operation.Expectation, obs=obs)

        # Non-involutory observables are present; the partial derivative of <A^2>
        # may be non-zero. Here, we calculate the analytic derivatives of the <A^2>
        # observables.
        gradient_sq_tapes, grad_sq_fn = parameter_shift_gradient(
            pdA2_tape, idx, gradient_recipe=gradient_recipe
        )
        tapes.extend(gradient_sq_tapes)

    if expectation is None:
        tapes.append(unshifted_ev_tape)

    def processing_fn(results):
        """Computes the gradient of the parameter at index ``idx`` via the
        parameter-shift method for a circuit containing a mixture
        of expectation values and variances.

        Args:
            results (list[real]): evaluated quantum tapes

        Returns:
            array[float]: 1-dimensional array of length determined by the tape output
            measurement statistics
        """
        pdA = grad_fn(results[0:2])
        pdA2 = 0

        if non_involutory:
            pdA2 = grad_sq_fn(results[2:4])

            if involutory:
                pdA2[np.array(involutory)] = 0

        if expectation is None:
            # The expectation value hasn't been previously calculated;
            # it will be the last element of the `results` argument.
            expectation = np.array(results[-1])

        # return d(var(A))/dp = d<A^2>/dp -2 * <A> * d<A>/dp for the variances,
        # d<A>/dp for plain expectations
        return np.where(var_mask, pdA2 - 2 * expectation * pdA, pdA)

    return tapes, processing_fn
