# coding=utf-8
# Copyright 2020 The TF-Agents Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Lint as: python3
"""Utils for distributed training using Actor/Learner API."""

import os
import time
from typing import Callable, Text, Tuple

from absl import logging

import tensorflow.compat.v2 as tf

from tf_agents.agents import tf_agent
from tf_agents.policies import py_tf_eager_policy
from tf_agents.typing import types
from tf_agents.utils import lazy_loader

# Lazy loading since not all users have the reverb package installed.
reverb = lazy_loader.LazyLoader('reverb', globals(), 'reverb')

# By default the implementation of wait functions blocks with relatively large
# number of frequent retries assuming that the event usually happens soon, but
# occasionally takes longer.
_WAIT_DEFAULT_SLEEP_TIME_SECS = 1
_WAIT_DEFAULT_NUM_RETRIES = 60 * 60 * 24  # 1 day


def create_train_step() -> tf.Variable:
  return tf.Variable(
      0,
      trainable=False,
      dtype=tf.int64,
      aggregation=tf.VariableAggregation.ONLY_FIRST_REPLICA,
      shape=())


def create_staleness_metrics_after_train_step_fn(
    train_step: tf.Variable,
    train_steps_per_policy_update: int = 1
) -> Callable[
    [Tuple[types.NestedTensor,
           types.ReverbSampleInfo], tf_agent.LossInfo], None]:
  """Creates an `after_train_step_fn` that computes staleness summaries.

  Staleness, in this context, means that the observation was generated by a
  policy that is older than the recently outputed policy.
  Assume that observation train step is stored as Reverb priorities.

  Args:
    train_step: The current train step.
    train_steps_per_policy_update: Number of train iterations to perform between
      two policy updates.

  Returns:
    The created `after_train_step_fn`.
  """

  def after_train_step_fn(experience, loss_info):
    del loss_info  # Unused.
    _, sample_info = experience

    # Get the train step in which the experience was observed. This is stored as
    # Reverb priority.
    # TODO(b/168426331): Check sample info version.
    observation_generation_train_step = tf.cast(
        sample_info.priority, dtype=tf.int64)

    # Get the train step corresponding to the latest outputed policy.
    # Policy is written in every `train_steps_per_policy_update` step, so we
    # normalize the value of `train_step` accordingly.
    on_policy_train_step = tf.cast(
        train_step / train_steps_per_policy_update,
        dtype=tf.int64) * train_steps_per_policy_update

    # An observation is off-policy if its train step delta is greater than 0.
    observation_train_step_delta = (
        on_policy_train_step - observation_generation_train_step)
    max_train_step_delta = tf.reduce_max(observation_train_step_delta)
    max_policy_update_delta = tf.cast(
        max_train_step_delta / train_steps_per_policy_update, dtype=tf.int64)
    num_stale_observations = tf.reduce_sum(
        tf.cast(observation_train_step_delta > 0, tf.int64))

    # Break out from local name scopes (e.g. the ones intrdouced by while loop).
    with tf.name_scope(''):
      # Write the summaries for the first replica.
      tf.summary.scalar(
          name='staleness/max_train_step_delta_in_batch',
          data=max_train_step_delta,
          step=train_step)
      tf.summary.scalar(
          name='staleness/max_policy_update_delta_in_batch',
          data=max_policy_update_delta,
          step=train_step)
      tf.summary.scalar(
          name='staleness/num_stale_obserations_in_batch',
          data=num_stale_observations,
          step=train_step)

  return after_train_step_fn


def wait_for_policy(
    policy_dir: Text,
    sleep_time_secs: int = _WAIT_DEFAULT_SLEEP_TIME_SECS,
    num_retries: int = _WAIT_DEFAULT_NUM_RETRIES,
    **saved_model_policy_args) -> py_tf_eager_policy.PyTFEagerPolicyBase:
  """Blocks until the policy in `policy_dir` becomes available.

  The default setting allows a fairly loose, but not infinite wait time of one
  days for this function to block checking the `policy_dir` in every seconds.

  Args:
    policy_dir: The directory containing the policy files.
    sleep_time_secs: Number of time in seconds slept between retries.
    num_retries: Number of times the existence of the file is checked.
    **saved_model_policy_args: Additional keyword arguments passed directly to
      the `SavedModelPyTFEagerPolicy` policy constructor which loads the policy
      from `policy_dir` once the policy becomes available.

  Returns:
    The policy loaded from the `policy_dir`.

  Raises:
    TimeoutError: If the policy does not become available during the number of
      retries.
  """
  # TODO(b/173815037): Write and wait for a DONE file instead.
  last_written_policy_file = os.path.join(policy_dir, 'policy_specs.pbtxt')
  wait_for_file(
      last_written_policy_file,
      sleep_time_secs=sleep_time_secs,
      num_retries=num_retries)
  return py_tf_eager_policy.SavedModelPyTFEagerPolicy(policy_dir,
                                                      **saved_model_policy_args)


# TODO(b/142821173): Test train_utils `wait_for_files` function.
def wait_for_file(file_path: Text,
                  sleep_time_secs: int = _WAIT_DEFAULT_SLEEP_TIME_SECS,
                  num_retries: int = _WAIT_DEFAULT_NUM_RETRIES) -> Text:
  """Blocks until the file at `file_path` becomes available.

  The default setting allows a fairly loose, but not infinite wait time of one
  days for this function to block checking the `file_path` in every seconds.

  Args:
    file_path: The path to the file that we are waiting for.
    sleep_time_secs: Number of time in seconds slept between retries.
    num_retries: Number of times the existence of the file is checked.

  Returns:
    The original `file_path`.

  Raises:
    TimeoutError: If the file does not become available during the number of
      trials.
  """

  def _is_file_missing(file_path=file_path):
    """Checks if the file is (still) missing, i.e. more wait is necessary."""
    try:
      stat = tf.io.gfile.stat(file_path)
    except tf.errors.NotFoundError:
      return True
    return stat.length <= 0

  wait_for_predicate(
      wait_predicate_fn=_is_file_missing,
      sleep_time_secs=sleep_time_secs,
      num_retries=num_retries)

  return file_path


# TODO(b/142821173): Test train_utils `wait_for_predicate` function.
def wait_for_predicate(wait_predicate_fn: Callable[[], bool],
                       sleep_time_secs: int = _WAIT_DEFAULT_SLEEP_TIME_SECS,
                       num_retries: int = _WAIT_DEFAULT_NUM_RETRIES) -> None:
  """Blocks while `wait_predicate_fn` is returning `True`.

  The callable `wait_predicate_fn` indicates if waiting is still needed by
  returning `True`. Once the condition that we wanted to wait for met, the
  callable should return `False` denoting that the execution can continue.

  The default setting allows a fairly loose, but not infinite wait time of one
  days for this function to block checking the `wait_predicate_fn` in every
  seconds.

  Args:
    wait_predicate_fn: A callable returning a bool. Blocks while it is returning
      `True`. Returns if it becomes `False`.
    sleep_time_secs: Number of time in seconds slept between retries.
    num_retries: Number of times the existence of the file is checked.

  Raises:
    TimeoutError: If the `wait_predicate_fn` does not become `False` during the
      number of trials.
  """
  retry = 0
  while (num_retries is None or retry < num_retries) and wait_predicate_fn():
    if sleep_time_secs > 0:
      logging.info(
          'Waiting for `wait_predicate_fn`. Block execution. Sleeping for %d '
          'seconds.', sleep_time_secs)
      time.sleep(sleep_time_secs)
    retry += 1

  if retry >= num_retries:
    raise TimeoutError(
        'The wait predicate did not return `False` after {} retries waiting {} '
        'seconds between retries.'.format(num_retries, sleep_time_secs))

  logging.info('The `wait_predicate_fn` returned `False`. Continue execution.')
