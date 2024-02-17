class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        losses = {}

        for winner, loser in matches:
            losses[loser] = losses.get(loser, 0) + 1
            if winner not in losses:
                losses[winner] = 0

        not_lost = []
        one_loss = []
        for player, loss_count in losses.items():
            if loss_count == 0:
                not_lost.append(player)
            elif loss_count == 1:
                one_loss.append(player)

        return [sorted(not_lost), sorted(one_loss)]
