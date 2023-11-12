from thor_devkit.cry import mnemonic
from retro_bip_utils import Bip32

VET_PATH = "m/44'/818'/0'/0"

def _get_key_path(base_path: str, index: int = 0) -> str:
    return base_path.rstrip('/') + '/' + str(index)

def _get_vet_key_path(index: int = 0) -> str:
    return _get_key_path(VET_PATH, index)

# TODO: Replace mnemonics
# Example: words = ['denial', 'kitchen', 'pet', 'squirrel', 'other', 'broom', 'bar', 'gas', 'better', 'priority', 'spoil', 'cross']
words = []

flag = mnemonic.validate(words)

if flag:
    # Get a Bip32 master seed for HD wallets
    seed = mnemonic.derive_seed(words)

    # Get private key
    bip32_ctx = Bip32.FromSeedAndPath(seed, _get_vet_key_path())
    private_key = bip32_ctx.PrivateKey().Raw().ToHex()
    print(private_key)

else:
    print("Error: Invalid mnemonics!")
