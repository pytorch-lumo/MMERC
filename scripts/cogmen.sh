for seed in {1..3}; do
  for m in 'a' 't' 'v' 'atv' 'av' 'at' 'tv'; do
    python3 train_mm.py --module=cogmen --dataset=iemocap-cogmen-robert-4 --modality=$m --reimplement --seed=$seed --device=0 &
    python3 train_mm.py --module=cogmen --dataset=iemocap-cogmen-sbert-4 --modality=$m --reimplement --seed=$seed --device=1 &
    python3 train_mm.py --module=cogmen --dataset=iemocap-cogmen-4 --modality=$m --reimplement --seed=$seed --device=2 &
    python3 train_mm.py --module=cogmen --dataset=iemocap-cogmen-tsn-4 --modality=$m --reimplement --seed=$seed --device=3 &
    python3 train_mm.py --module=cogmen --dataset=iemocap-cogmen-robert-6 --modality=$m --reimplement --seed=$seed --device=4 &
    python3 train_mm.py --module=cogmen --dataset=iemocap-cogmen-sbert-6 --modality=$m --reimplement --seed=$seed --device=5 &
    python3 train_mm.py --module=cogmen --dataset=iemocap-cogmen-6 --modality=$m --reimplement --seed=$seed --device=6 &
    python3 train_mm.py --module=cogmen --dataset=iemocap-cogmen-tsn-6 --modality=$m --reimplement --seed=$seed --device=7 &
    wait
  done
done