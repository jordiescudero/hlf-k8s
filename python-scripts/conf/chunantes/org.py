from .peers.peer1 import peer1
from .peers.peer2 import peer2
from .users.admin import admin
from .users.bootstrap_admin import bootstrap_admin
from .users.user import user

chunantes = {
    'name': 'chu-nantes',
    'msp_id': 'chu-nantesMSP',
    'anchor_tx_file': '/substra/data/orgs/chu-nantes/anchors.tx',
    'tls': {
        # careful, `ca-cert.pem` is the default cert name file and a example file with this name is already present in the docker image, do not forget to remove these examples files if naming the same way
        'certfile': '/substra/data/orgs/chu-nantes/tls-ca-cert.pem',
        'clientkey': ''
    },
    'ca': {
        'name': 'rca-chu-nantes',
        'host': 'rca-chu-nantes',
        'certfile': '/substra/data/orgs/chu-nantes/ca-cert.pem',
        'keyfile': '/substra/data/orgs/chu-nantes/ca-key.pem',
        'port': {
            'internal': 7054,
            'external': 8054
        },
        'url': 'https://rca-chu-nantes:7054',
        'logfile': '/substra/data/log/rca-chu-nantes.log',
        'server-config-path': '/substra/conf/chu-nantes/fabric-ca-server-config.yaml',
        'client-config-path': '/substra/conf/chu-nantes/fabric-ca-client-config.yaml',
    },
    'users': {
        'bootstrap_admin': bootstrap_admin,
        'admin': admin,
        'user': user,
    },
    'csr': {
        'cn': 'rca-chu-nantes',
        # The "hosts" value is a list of the domain names which the certificate should be valid for.
        'hosts': ['rca-chu-nantes']
    },
    'core': {
        'docker': {
            'peer_home': '/etc/hyperledger/fabric/',
            'msp_config_path': '/etc/hyperledger/fabric/msp',
        },
        'host': {
            'peer_home': '/substra/data/orgs/chu-nantes',
            'msp_config_path': '/substra/data/orgs/chu-nantes/user/msp',
        }
    },
    'core_dir': {
        'internal': '/etc/hyperledger/fabric',
        'external': '/substra/data/orgs/chu-nantes'
    },
    'peers': [peer1, peer2]
}
