# Copyright 2021 Iguazio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from nuclio.triggers import HttpTrigger


def test_cast_http_trigger_port_to_int():
    http_trigger = HttpTrigger(port='9009')
    assert http_trigger.get_port == 9009


def test_http_trigger_no_port():
    http_trigger = HttpTrigger()
    assert http_trigger.get_port is None


def test_http_trigger_workers_to_int():
    http_trigger = HttpTrigger(host='something')
    http_trigger.workers('123')
    assert http_trigger.get_workers == 123


def test_http_trigger_host():
    http_trigger = HttpTrigger(host='something', paths=['/here'])
    assert http_trigger.get_ingresses['0'].get('host') == 'something'
    assert http_trigger.get_ingresses['0'].get('paths') == ['/here']
