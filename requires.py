#
# Copyright (c) 2016 Midokura SARL, All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from charms.reactive import RelationBase
from charms.reactive import hook
from charms.reactive import scopes


class MidonetApiRequires(RelationBase):
    scope = scopes.GLOBAL

    auto_accessors = ['host', 'port']

    @hook('{requires:midonet-api}-relation-{joined,changed}')
    def changed(self):
        self.set_state('{relation_name}.connected')
        if self.connection_data():
            self.set_state('{relation_name}.available')

    @hook('{requires:midonet-api}-relation-{departed,broken}')
    def departed(self):
        conv = self.conversation()
        conv.remove_state('{relation_name}.available')
        conv.remove_state('{relation_name}.connected')

    def connection_data(self):
        """Returns a tuple of host address and port."""
        host = self.host()
        port = self.port()
        if host and port:
            return host, port
        return None
