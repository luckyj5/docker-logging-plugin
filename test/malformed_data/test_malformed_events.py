import pytest
import time
import uuid
import logging
<<<<<<< HEAD
import sys
from common import open_fifo,\
    write_proto_buf_message, request_start_logging, \
    check_events_from_splunk, request_stop_logging, \
    close_fifo

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)


@pytest.mark.parametrize("test_input,expected", [
    ("", 0),  # should not be sent to splunk
    (" ", 0),  # should not be sent to splunk
    ("\xF0\xA4\xAD", 1),  # non utf-8 decodable chars should still make it to splunk
    ("hello", 1),  # normal string should always to sent to splunk
    ("{'test': 'incomplete}", 1) # malformed json string should still be sent to splunk
=======
from ..common import request_start_logging,  \
    check_events_from_splunk, request_stop_logging, \
    start_log_producer_from_input


@pytest.mark.parametrize("test_input,expected", [
    ([("", False)], 0),  # should not be sent to splunk
    ([(" ", False)], 0),  # should not be sent to splunk
    ([("\xF0\xA4\xAD", False)], 1),  # non utf-8 decodable chars
                                     # should make it to splunk
    ([("hello", False)], 1),  # normal string should always to sent to splunk
    ([("{'test': 'incomplete}", False)], 1)  # malformed json string should
                                             # be sent to splunk
>>>>>>> 8ad8f7e575a88fc85cc6520d140f8f1b311b88cd
])
def test_malformed_empty_string(setup, test_input, expected):
    '''
    Test that the logging plugin can handle various type of input correctly.
    Expected behavior is that:
        * Empty string or string with only spaces should be neglected
        * Non empty strings should be sent to Splunk
        * Non UTF-8 decodable string should still be sent to Splunk
    '''
<<<<<<< HEAD
    logger.info("testing test_malformed_empty_string input={0} \
=======
    logging.getLogger().info("testing test_malformed_empty_string input={0} \
>>>>>>> 8ad8f7e575a88fc85cc6520d140f8f1b311b88cd
                expected={1} event(s)".format(test_input, expected))
    u_id = str(uuid.uuid4())

    file_path = setup["fifo_path"]
<<<<<<< HEAD
    f_writer = open_fifo(file_path)

    logger.info("Writing data in protobuf with source=%s", u_id)
    write_proto_buf_message(f_writer, message=test_input, source=u_id)
    close_fifo(f_writer)

    request_start_logging(file_path, setup["splunk_hec_url"], setup["splunk_hec_token"])
=======
    start_log_producer_from_input(file_path, test_input, u_id)

    request_start_logging(file_path,
                          setup["splunk_hec_url"],
                          setup["splunk_hec_token"])
>>>>>>> 8ad8f7e575a88fc85cc6520d140f8f1b311b88cd

    # wait for 10 seconds to allow messages to be sent
    time.sleep(10)
    request_stop_logging(file_path)

    # check that events get to splunk
    events = check_events_from_splunk(id=u_id,
                                      start_time="-1m@m",
                                      url=setup["splunkd_url"],
                                      user=setup["splunk_user"],
                                      password=setup["splunk_password"])
<<<<<<< HEAD
    logger.info("Splunk received %s events in the last minute with u_id=%s",
                len(events), u_id)
=======
    logging.getLogger().info("Splunk received %s events in the last minute " +
                             "with u_id=%s",
                             len(events), u_id)
>>>>>>> 8ad8f7e575a88fc85cc6520d140f8f1b311b88cd
    assert len(events) == expected
