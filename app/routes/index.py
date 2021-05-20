from datetime import datetime
from fastapi import APIRouter
from starlette.responses import Response
from Bio import SeqIO
from ..common import config


router = APIRouter()


@router.get("/")
async def index():
    """
    상태 체크용 API
    """
    current_time = datetime.utcnow()
    return Response(f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})")


@router.get("/test")
async def test():
    """
    genbank file read API
    """
    print(config.base_dir)

    target_dir = config.base_dir + '\\data\\'
    result = []
    for seq_record in SeqIO.parse(target_dir + "ls_orchid.gbk", "genbank"):
        count_a = seq_record.seq.count('A')
        count_t = seq_record.seq.count('T')
        count_c = seq_record.seq.count('C')
        count_g = seq_record.seq.count('G')
        total_len = len(seq_record)
        dic = {"id": seq_record.id, "seq": repr(seq_record.seq),
               "length": total_len,
               "count_A": count_a,
               "percent_A": round(count_a/total_len*100, 2),
               "count_T": count_t,
               "percent_T": round(count_t/total_len*100, 2),
               "count_C": count_c,
               "percent_C": round(count_c/total_len*100, 2),
               "count_G": count_g,
               "percent_G": round(count_g/total_len*100, 2),
               }
        result.append(dic)

    return result
