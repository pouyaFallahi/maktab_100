import unittest, threading, time, subprocess

def run_server():
    subprocess.run(['python', 'server.py'])

class TestClientServer(unittest.TestCase):
    @classmethod
    def set_up_class(cls):
        cls.server_thread = threading.Thread(target=run_server())
        cls.server_thread.start()
        time.sleep(1)


    @classmethod
    def tear_down_class(cls):
        subprocess.run(['pkill','-f', 'weather_server.py'])
        cls.server_thread.join()

    def test_client_server_communication(self):
        result = subprocess.run(['python', 'weather_client.py'], capture_output=True, text=True)
        output = result.stdout.strip()
        expexted_output = ''
        self.assertEqual(output, expexted_output)


if __name__ == '__main__':
    unittest.main()
