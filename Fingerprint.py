import bech32 as bech
from hashlib import blake2b

class FingerPrint:
    def getFingerPrint(self, combined):
        hash = blake2b(combined, digest_size=20).digest()
        assetFingerPrint = bech.encode(witprog= hash, hrp='asset')
        return assetFingerPrint

    def getAssetFingerPrint(self, policy, assetName):
        bytePolicy = bytearray.fromhex(policy)
        byteAssetName = bytearray.fromhex(assetName)
        return self.getFingerPrint(bytePolicy + byteAssetName)

    def getPrimaryFingerPrint(self, blockNumber, policy, assetName):
        bytePolicy = bytearray.fromhex(policy)
        byteAssetName = bytearray.fromhex(assetName)
        byteBlockNumber = bytearray.fromhex(blockNumber)
        print(self.getFingerPrint(bytePolicy + byteAssetName + byteBlockNumber))
    def testAssetFingerPrint(self):
        policies = [
            "7eae28af2208be856f7a119668ae52a49b73725e326dc16579dcc373",
            "7eae28af2208be856f7a119668ae52a49b73725e326dc16579dcc37e",
            "7eae28af2208be856f7a119668ae52a49b73725e326dc16579dcc373",
            "1e349c9bdea19fd6c147626a5260bc44b71635f398b67c59881df209",
            "7eae28af2208be856f7a119668ae52a49b73725e326dc16579dcc373"
        ]
        assetNames = [
            "",
            "",
            "504154415445",
            "504154415445",
            "0000000000000000000000000000000000000000000000000000000000000000"
        ]
        results = [
            "asset1rjklcrnsdzqp65wjgrg55sy9723kw09mlgvlc3",
            "asset1nl0puwxmhas8fawxp8nx4e2q3wekg969n2auw3",
            "asset13n25uv0yaf5kus35fm2k86cqy60z58d9xmde92",
            "asset1hv4p5tv2a837mzqrst04d0dcptdjmluqvdx9k3",
            "asset1pkpwyknlvul7az0xx8czhl60pyel45rpje4z8w"
        ]

        for i in range(len(policies)):
            assetFingerPrint = self.getAssetFingerPrint(policies[i], assetNames[i])
            assert results[i] == assetFingerPrint
            print(results[i] == assetFingerPrint)
if __name__ == '__main__':
    fingerPrint = FingerPrint()
    fingerPrint.testAssetFingerPrint()
