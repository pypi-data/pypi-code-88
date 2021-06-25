### 아직 적용하지 않음.


import sys, os
PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(PROJECT_ROOT)

import time
import re
import os
import argparse
from multiprocessing import Process, cpu_count, Queue

from codes.codes_db import get_all_corps_codes
from corps.handle_db.corps_df import CorpDF
from corps.handle_db import corps_db
from corps.scraper import use_multi, spiders
from sa_setting import logger, CORPDB_PATH, flush_log


class RepairCorps:
    full_tables = (
        'c103손익계산서q',
        'c103손익계산서y',
        'c103재무상태표q',
        'c103재무상태표y',
        'c103현금흐름표q',
        'c103현금흐름표y',
        'c104가치분석q',
        'c104가치분석y',
        'c104성장성q',
        'c104성장성y',
        'c104수익성q',
        'c104수익성y',
        'c104안정성q',
        'c104안정성y',
        'c104활동성q',
        'c104활동성y',
        'c106y',
        'c106q',
        'c101',
    )

    @staticmethod
    def _chk_dfs(codes, q):
        fails = []
        total_num = len(codes)
        for i, code in enumerate(codes):
            for table in RepairCorps.full_tables:
                try:
                    # 테이블이 비어있는 경우
                    if CorpDF(code, table).df.empty:
                        fails.append(code)
                        logger.info(f'{code} : {table} is empty')
                except RuntimeError:
                    # 테이블 자체가 없어서 RuntimeError 발생한 경우
                    fails.append(code)
                    logger.info(f'{code} : {table} not exists')
            print(f'{i + 1} / {total_num}')
        q.put(fails)

    @staticmethod
    def _chk_c101name(codes, q):
        # 간혹 같은 코드번호를 사용하고 회사만 변경되는 경우를 찾아내기 위해..
        fails = []
        total_num = len(codes)
        for i, code in enumerate(codes):
            print(f'{i + 1} / {total_num}')
            try:
                c101 = CorpDF(code, 'c101')
            except RuntimeError:
                fails.append(code)
                continue
            try:
                # print(code, set(c101.get_dict_by_column('종목명').values()))
                if len(set(c101.get_dict_by_column('종목명').values())) != 1:
                    fails.append(code)
            except AttributeError:
                # c101 테이블이 없는경우
                fails.append(code)

        q.put(fails)

    @staticmethod
    def mp_integrity(codes, func):
        def _code_divider(entire_codes):
            def split_list(alist, wanted_parts=1):
                # 멀티프로세싱할 갯수로 리스트를 나눈다.
                # reference from https://www.it-swarm.dev/ko/python/%EB%8D%94-%EC%9E%91%EC%9D%80-%EB%AA%A9%EB%A1%9D%EC%9C%BC%EB%A1%9C-%EB%B6%84%ED%95%A0-%EB%B0%98%EC%9C%BC%EB%A1%9C-%EB%B6%84%ED%95%A0/957910776/
                length = len(alist)
                return [alist[i * length // wanted_parts: (i + 1) * length // wanted_parts]
                        for i in range(wanted_parts)]

            # reference from https://stackoverflow.com/questions/19086106/how-to-utilize-all-cores-with-python-multiprocessing
            core = cpu_count()
            print(f'Get number of core for multiprocessing : {core}')
            n = core - 1
            if len(entire_codes) < n:
                n = len(entire_codes)
            print(f'Split total {len(entire_codes)} codes by {n} parts ...')
            divided_list = split_list(entire_codes, wanted_parts=n)
            return n, divided_list

        # 전체 코드를 코어수대로 나눠서 멀티프로세싱 시행
        # spider - ['c101','c103','c104','c106','c108']
        print('*' * 25, f"Checking with '{func.__name__}' ", '*' * 25)
        n, divided_list = _code_divider(codes)

        start_time = time.time()
        # 큐를 통해서 fail_list를 취합한다.
        q = Queue()
        ths = []
        for i in range(n):
            ths.append(Process(target=func, args=(divided_list[i], q)))
        for i in range(n):
            ths[i].start()
        total_fails = []
        for i in range(n):
            total_fails += q.get()
        for i in range(n):
            ths[i].join()
        logger.info(f"'{func.__name__}' fails : {total_fails}")
        print(f'Total spent time : {round(time.time() - start_time, 2)} sec')
        return set(total_fails)

    @staticmethod
    def check_n_repair():
        all_codes = get_all_corps_codes()
        fails_c101 = RepairCorps.mp_integrity(all_codes, RepairCorps._chk_c101name)
        print(f"'fails c101 : {fails_c101}")
        for code in fails_c101:
            corps_db.drop_table(corps_db.make_engine(code), 'c101')
            use_multi('c101', code)
        fails = RepairCorps.mp_integrity(all_codes, RepairCorps._chk_dfs)
        print(f"'fails df : {fails}")
        for code in fails:
            for spider in spiders:
                use_multi(spider, code)
        return fails_c101 | fails


class SyncCorps:
    @staticmethod
    def cleaning_corps_folder():
        # 정규표현식으로 6자리 숫자 형식의 파일명인지 확인하여 아니면 삭제한다.
        print('*' * 25, '1. Check integrity corp_db filename', '*' * 25, flush=True)
        p = re.compile('[0-9][0-9][0-9][0-9][0-9][0-9]')
        for path, _, files in os.walk(CORPDB_PATH):
            logger.info(f'path : {path}')
            logger.info(f'files : {files}')
            for filename in files:
                if not p.match(os.path.splitext(filename)[0]):
                    os.remove(os.path.join(path, filename))
                    logger.error(f'Invalid filename : {filename}')
                    print(f'\tDelete {filename}..')
        print('Done.')

    @staticmethod
    def sync_db_and_folder():
        # codes.db의 krx테이블과 corp_db의 파일을 맞춰줌.
        print('*' * 20, '2.Sync with codes.db and copr_db folder', '*' * 20, flush=True)
        for path, _, files in os.walk(CORPDB_PATH):
            codes = get_all_corps_codes()
            print('\tThe number of codes in codes.db(krx table): ', len(codes))
            # 파일명에서 확장자를 제거한다.
            filenames = list(map(lambda x: os.path.splitext(x)[0], files))
            logger.debug(filenames)
            del_targets = list(set(filenames) - set(codes))
            add_targets = list(set(codes) - set(filenames))
            logger.info(f'Delete target: {del_targets}')
            logger.info(f'Add target: {add_targets}')
            print('\tDelete target: ', del_targets)
            print('\tAdd target: ', add_targets)

            for full_path in list(map(lambda x: os.path.join(path, x + '.db'), del_targets)):
                os.remove(full_path)
                print(f'\tDelete {full_path}..')

            for code in add_targets:
                for spider in ['c103', 'c104']:
                    use_multi(spider, code)
        print('Done.')
        return add_targets, del_targets

    @staticmethod
    def start():
        SyncCorps.cleaning_corps_folder()
        return SyncCorps.sync_db_and_folder()


if __name__ == '__main__':
    # reference form https://docs.python.org/3.3/howto/argparse.html#id1
    parser = argparse.ArgumentParser()
    parser.add_argument('cmd', help="repair or sync")
    parser.add_argument('-m', '--message', action='store_true', help='Send telegram message with result after work.')

    args = parser.parse_args()

    if args.cmd == 'repair':
        fail_codes = RepairCorps.check_n_repair()
        if args.message:
            flush_log(f'>>> python repairman.py {args.cmd} -m\n'
                      f'repaired codes : {fail_codes}')
    elif args.cmd == 'sync':
        add_codes, del_codes = SyncCorps.start()
        if args.message:
            flush_log(f'>>> python repairman.py {args.cmd} -m\n'
                      f'add : {add_codes}\n'
                      f'del : {del_codes}')
    else:
        parser.print_help()
