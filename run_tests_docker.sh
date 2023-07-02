docker run \
--env-file=variables_local_docker.env \
--env-file=credential_local_docker.env \
-v /Users/bruktawitmekuria/QA_live_class/Framework_Project/ecomstore:/automation/ecomstore \
--network=host \
poineers_fm:1.0 --color=yes

