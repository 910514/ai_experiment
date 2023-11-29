ai實驗成果
/usr/local/lib/python3.10/dist-packages/gradio_client/utils.py
@staticmethod
    def msg_to_status(msg: str) -> Status:
        """Map the raw message from the backend to the status code presented to users."""
        return {
            "send_hash": Status.JOINING_QUEUE,
            "queue_full": Status.QUEUE_FULL,
            "estimation": Status.IN_QUEUE,
            "send_data": Status.SENDING_DATA,
            "process_starts": Status.PROCESSING,
            "process_generating": Status.ITERATING,
            "process_completed": Status.FINISHED,
            "progress": Status.PROGRESS,
            "heartbeat": Status.PROGRESS,      # add this line
        }[msg]
