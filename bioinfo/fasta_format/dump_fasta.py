from pathlib import Path
import shutil
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


def dump_fasta(file_path, seq_list, with_txt=False):
    assert isinstance(seq_list, dict) or isinstance(seq_list, list)
    if isinstance(seq_list, dict):
        # TODO: sort the list?
        seq_list = [
                SeqRecord(
                    id=str(k),
                    seq=Seq(v),
                    description=''
                )
                for k, v in seq_list.items()
            ]
    elif isinstance(seq_list, list):
        seq_list = [
                SeqRecord(
                    id=str(k),
                    seq=Seq(v),
                    description=''
                )
                for k, v in seq_list
            ]

    file_path = Path(file_path)
    file_path.parent.mkdir(exist_ok=True, parents=True)

    SeqIO.write(
        seq_list,
        str(file_path),
        'fasta')

    if with_txt:
        txt_path = file_path.stem + '.txt'
        shutil.copy(
            str(file_path),
            str(txt_path)
        )
