config = dict(
    trees=['rawhide', 'f21'],
    fedmsg_atomic_composer=True,
    config_key='fedmsg_atomic_composer',
    topic = ['org.fedoraproject.prod.bodhi.updates.fedora.sync',
             'org.fedoraproject.prod.compose.branched.rsync.complete',
             'org.fedoraproject.prod.compose.rawhide.rsync.complete',
             'org.fedoraproject.stg.bodhi.updates.fedora.sync',
             'org.fedoraproject.stg.compose.branched.rsync.complete',
             'org.fedoraproject.stg.compose.rawhide.rsync.complete',
             'org.fedoraproject.dev.bodhi.updates.fedora.sync',
             'org.fedoraproject.dev.compose.branched.rsync.complete',
             'org.fedoraproject.dev.compose.rawhide.rsync.complete'],
    touch_dir='/srv/inbox/',
    output_dir='/srv/fedora-atomic/output/',
    production_repos='localhost:/srv/production/',
    local_repos='/srv/fedora-atomic/',
)
