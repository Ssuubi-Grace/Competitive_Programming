class FrequencyTracker(object):

    def __init__(self):
        """
        Initializes the frequency tracker with an empty dictionary to store frequency counts.
        """
        self.freq_counts = {}

    def add(self, number):
        """
        Adds the given number to the tracker and updates its frequency count.

        Args:
            number: The integer to add.
        """
        self.freq_counts[number] = self.freq_counts.get(number, 0) + 1

    def deleteOne(self, number):
        """
        Deletes one occurrence of the given number from the tracker if it exists.

        Args:
            number: The integer to delete.
        """
        if number in self.freq_counts:
            self.freq_counts[number] -= 1
            if self.freq_counts[number] == 0:
                del self.freq_counts[number]

    def hasFrequency(self, frequency):
        """
        Checks if there exists a number in the tracker that occurs the given frequency.

        Args:
            frequency: The target frequency to check.

        Returns:
            True if a number with the given frequency exists, False otherwise.
        """
        return any(count == frequency for count in self.freq_counts.values())
