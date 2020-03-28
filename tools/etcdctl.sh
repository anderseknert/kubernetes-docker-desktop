#!/usr/bin/env bash
#
# Helper script to query etcd.
#
# Usage instructions:
#
# List all keys
# ./etcdctl.sh get / --prefix --keys-only
#
# Read an object by key
# ./etcdctl.sh get /registry/secrets/default/common-env-secrets
#
# Delete an object by key
# ./etcdctl.sh del /registry/secrets/default/common-env-secrets
#
kubectl -n kube-system exec etcd-docker-desktop -- env ETCDCTL_API=3 etcdctl \
    --key /run/config/pki/etcd/peer.key \
    --cert /run/config/pki/etcd/peer.crt \
    --cacert /run/config/pki/etcd/ca.crt "$@"