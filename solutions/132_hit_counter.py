#!/usr/bin/python

"""
This question was asked by Riot Games.

Design and implement a HitCounter class that keeps track of requests (or hits). It should support the following operations:

    record(timestamp): records a hit that happened at timestamp
    total(): returns the total number of hits recorded
    range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)

Follow-up: What if our system has limited memory?

"""
import random,bisect

REQUESTSPERFILE=100

# In a memory efficient implmentation, this would be persisted to disk
# once full and only the path and metadata would remain in memory
class PersistedFile:
    def __init__(self):
        self.start_timestamp=None
        self.end_timestamp=None
        self.request_timestamps=list()

    def __repr__(self):
        return "start={}, end={}, size={}".format(self.start_timestamp,self.end_timestamp,len(self.request_timestamps))

    def total(self):
        return len(self.request_timestamps)

    def record(self,timestamp):
        if not self.start_timestamp:
            self.start_timestamp=timestamp

        self.end_timestamp=timestamp
        self.request_timestamps.append(timestamp)

    def save_to_file(self):
        # save to file
        pass

class HitCounter:
    def __init__(self):
        self.current_file=PersistedFile()
        self.prev_files=list()

    def record(self,timestamp):
        self.current_file.record(timestamp)

        if self.current_file.total() >= REQUESTSPERFILE:
            self.current_file.save_to_file()
            self.prev_files.append(self.current_file)
            self.current_file=PersistedFile()

        return True

    def total(self):
        return REQUESTSPERFILE * len(self.prev_files) + self.current_file.total()

    def range(self,lower,upper):
        all_files=self.prev_files + [self.current_file]
        start_times=[file.start_timestamp for file in all_files ]
        end_times=[file.end_timestamp for file in all_files ]

        start_file_index=bisect.bisect_left(start_times,lower)-1
        end_file_index=bisect.bisect_left(end_times,upper)

        start_file=all_files[start_file_index]
        end_file=all_files[end_file_index]

        start_file_pos=bisect.bisect_left(start_file.request_timestamps, lower)
        end_file_pos=bisect.bisect_left(end_file.request_timestamps, upper)

        num_req=0
        num_req += len(start_file.request_timestamps[start_file_pos:])
        num_req += len(end_file.request_timestamps[:end_file_pos])
        num_req += (end_file_index - start_file_index) * REQUESTSPERFILE

        return num_req

def run_experiments(requests):
    rq = HitCounter()
    lower, upper = None, None

    for i in range(requests):
        rq.record(i)

        if random.random() < 0.001:
            if not lower:
                lower = i
            else:
                upper = random.randrange(lower, i)

            if lower and upper:
                num_req = rq.range(lower, upper)
                print("{} requests made between {} and {}".format(
                    num_req, lower, upper))
                print("Total: {}".format(rq.total()))
                lower, upper = None, None


run_experiments(112367)
