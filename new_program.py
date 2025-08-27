2025-08-27 13:33:12.738 [info] [main] Log level: Info
2025-08-27 13:33:12.738 [info] [main] Validating found git in: "C:\Program Files\Git\cmd\git.exe"
2025-08-27 13:33:12.738 [info] [main] Validating found git in: "C:\Program Files (x86)\Git\cmd\git.exe"
2025-08-27 13:33:12.738 [info] [main] Validating found git in: "C:\Program Files\Git\cmd\git.exe"
2025-08-27 13:33:12.738 [info] [main] Validating found git in: "C:\Users\hhanu\AppData\Local\Programs\Git\cmd\git.exe"
2025-08-27 13:33:12.757 [info] [main] Validating found git in: "C:\Microsoft VS Code\Git\cmd\git.exe"
2025-08-27 13:33:12.866 [info] [main] Using git "2.51.0.windows.1" from "C:\Microsoft VS Code\Git\cmd\git.exe"
2025-08-27 13:33:12.867 [info] [Model][doInitialScan] Initial repository scan started
2025-08-27 13:33:15.404 [info] > git rev-parse --show-toplevel [2197ms]
2025-08-27 13:33:16.265 [info] > git rev-parse --git-dir --git-common-dir --show-superproject-working-tree [727ms]
2025-08-27 13:33:16.310 [info] [Model][openRepository] Opened repository (path): c:\Users\hhanu\OneDrive\Python\Unit 1
2025-08-27 13:33:16.311 [info] [Model][openRepository] Opened repository (real path): c:\Users\hhanu\OneDrive\Python\Unit 1
2025-08-27 13:33:16.311 [info] [Model][openRepository] Opened repository (kind): repository
2025-08-27 13:33:16.315 [info] [Model][doInitialScan] Initial repository scan completed - repositories (1), closed repositories (0), parent repositories (0), unsafe repositories (0)
2025-08-27 13:33:18.651 [info] > git show --textconv 2e88bccfb4ebe8df2cdd22f815dabfd847124e18:new_program.py [2326ms]
2025-08-27 13:33:18.655 [info] > git config --get commit.template [2156ms]
2025-08-27 13:33:18.655 [info] > git fetch [2345ms]
2025-08-27 13:33:18.657 [info] > git ls-tree -l 2e88bccfb4ebe8df2cdd22f815dabfd847124e18 -- new_program.py [2325ms]
2025-08-27 13:33:19.147 [info] > git check-ignore -v -z --stdin [467ms]
2025-08-27 13:33:19.150 [info] > git ls-tree -l 2e88bccfb4ebe8df2cdd22f815dabfd847124e18 -- new_program.py [211ms]
2025-08-27 13:33:19.152 [info] > git config --get commit.template [250ms]
2025-08-27 13:33:19.514 [info] > git show --textconv :new_program.py [327ms]
2025-08-27 13:33:19.518 [info] > git ls-files --stage -- new_program.py [324ms]
2025-08-27 13:33:19.531 [info] > git for-each-ref --format=%(refname)%00%(upstream:short)%00%(objectname)%00%(upstream:track)%00%(upstream:remotename)%00%(upstream:remoteref) --ignore-case refs/heads/main refs/remotes/main [501ms]
2025-08-27 13:33:20.208 [info] > git for-each-ref --format=%(refname)%00%(upstream:short)%00%(objectname)%00%(upstream:track)%00%(upstream:remotename)%00%(upstream:remoteref) --ignore-case refs/heads/main refs/remotes/main [670ms]
2025-08-27 13:33:20.217 [info] > git cat-file -s d857eaea8885b2f45a5ebf3f6ec045428c628491 [687ms]
2025-08-27 13:33:20.218 [info] > git for-each-ref --format=%(refname)%00%(upstream:short)%00%(objectname)%00%(upstream:track)%00%(upstream:remotename)%00%(upstream:remoteref) --ignore-case refs/heads/main refs/remotes/main [735ms]
2025-08-27 13:33:20.230 [info] > git config --get commit.template [105ms]
2025-08-27 13:33:20.474 [info] > git ls-files --stage -- new_program.py [225ms]
2025-08-27 13:33:20.482 [info] > git config --get --local branch.main.vscode-merge-base [265ms]
2025-08-27 13:33:20.483 [warning] [Git][config] git config failed: Failed to execute git
2025-08-27 13:33:20.512 [info] > git for-each-ref --format=%(refname)%00%(upstream:short)%00%(objectname)%00%(upstream:track)%00%(upstream:remotename)%00%(upstream:remoteref) --ignore-case refs/heads/main refs/remotes/main [232ms]
2025-08-27 13:33:20.814 [info] > git for-each-ref --sort -committerdate --format %(refname)%00%(objectname)%00%(*objectname) [289ms]
2025-08-27 13:33:20.816 [info] > git reflog main --grep-reflog=branch: Created from *. [328ms]
2025-08-27 13:33:20.822 [info] > git cat-file -s d857eaea8885b2f45a5ebf3f6ec045428c628491 [340ms]
2025-08-27 13:33:20.850 [info] > git status -z -uall [331ms]
2025-08-27 13:33:20.851 [info] > git config --get --local branch.main.github-pr-owner-number [286ms]
2025-08-27 13:33:20.851 [warning] [Git][config] git config failed: Failed to execute git
2025-08-27 13:33:21.174 [info] > git config --get --local branch.main.remote [311ms]
2025-08-27 13:33:21.174 [warning] [Git][config] git config failed: Failed to execute git
2025-08-27 13:33:21.206 [info] > git blame --root --incremental 2e88bccfb4ebe8df2cdd22f815dabfd847124e18 -- new_program.py [410ms]
2025-08-27 13:33:21.219 [info] > git symbolic-ref --short refs/remotes/Github/HEAD [397ms]
2025-08-27 13:33:21.219 [info] fatal: ref refs/remotes/Github/HEAD is not a symbolic ref
2025-08-27 13:33:21.219 [warning] [Repository][getDefaultBranch] Failed to get default branch details: Failed to execute git.
2025-08-27 13:33:21.328 [info] > git for-each-ref --format=%(refname)%00%(upstream:short)%00%(objectname)%00%(upstream:track)%00%(upstream:remotename)%00%(upstream:remoteref) --ignore-case refs/heads/main refs/remotes/main [371ms]
2025-08-27 13:33:21.328 [info] > git config --get commit.template [404ms]
2025-08-27 13:33:21.458 [info] > git config --get --local branch.main.merge [252ms]
2025-08-27 13:33:21.459 [warning] [Git][config] git config failed: Failed to execute git
2025-08-27 13:33:21.698 [info] > git status -z -uall [365ms]
2025-08-27 13:33:21.699 [info] > git for-each-ref --sort -committerdate --format %(refname)%00%(objectname)%00%(*objectname) [360ms]
2025-08-27 13:33:39.728 [info] > git for-each-ref --format=%(refname)%00%(upstream:short)%00%(objectname)%00%(upstream:track)%00%(upstream:remotename)%00%(upstream:remoteref) --ignore-case refs/heads/main refs/remotes/main [88ms]
2025-08-27 13:33:39.735 [info] > git config --get commit.template [99ms]
2025-08-27 13:33:39.812 [info] > git for-each-ref --sort -committerdate --format %(refname)%00%(objectname)%00%(*objectname) [69ms]
2025-08-27 13:33:39.813 [info] > git status -z -uall [75ms]
2025-08-27 13:33:44.939 [info] > git config --get commit.template [97ms]
2025-08-27 13:33:44.945 [info] > git for-each-ref --format=%(refname)%00%(upstream:short)%00%(objectname)%00%(upstream:track)%00%(upstream:remotename)%00%(upstream:remoteref) --ignore-case refs/heads/main refs/remotes/main [92ms]
2025-08-27 13:33:45.028 [info] > git status -z -uall [78ms]
2025-08-27 13:33:45.034 [info] > git for-each-ref --sort -committerdate --format %(refname)%00%(objectname)%00%(*objectname) [82ms]
2025-08-27 13:33:48.202 [info] > git show --textconv :new_program.py [119ms]
2025-08-27 13:33:48.206 [info] > git ls-files --stage -- new_program.py [118ms]
2025-08-27 13:33:48.267 [info] > git cat-file -s d857eaea8885b2f45a5ebf3f6ec045428c628491 [56ms]
2025-08-27 13:33:59.584 [info] > git show --textconv :new_program.py [231ms]
2025-08-27 13:33:59.594 [info] > git ls-files --stage -- new_program.py [236ms]
2025-08-27 13:33:59.685 [info] > git cat-file -s d857eaea8885b2f45a5ebf3f6ec045428c628491 [86ms]
2025-08-27 13:35:04.179 [info] > git config --get commit.template [98ms]
2025-08-27 13:35:04.186 [info] > git for-each-ref --format=%(refname)%00%(upstream:short)%00%(objectname)%00%(upstream:track)%00%(upstream:remotename)%00%(upstream:remoteref) --ignore-case refs/heads/main refs/remotes/main [96ms]
2025-08-27 13:35:04.265 [info] > git status -z -uall [76ms]
2025-08-27 13:35:04.268 [info] > git for-each-ref --sort -committerdate --format %(refname)%00%(objectname)%00%(*objectname) [74ms]
2025-08-27 13:35:09.225 [info] > git log --format=%H%n%aN%n%aE%n%at%n%ct%n%P%n%D%n%B -z --shortstat --diff-merges=first-parent -n50 --skip=0 --topo-order --decorate=full --stdin [119ms]
2025-08-27 13:35:09.520 [info] > git config --get commit.template [229ms]
2025-08-27 13:35:09.528 [info] > git for-each-ref --format=%(refname)%00%(upstream:short)%00%(objectname)%00%(upstream:track)%00%(upstream:remotename)%00%(upstream:remoteref) --ignore-case refs/heads/main refs/remotes/main [216ms]
2025-08-27 13:35:09.617 [info] > git for-each-ref --sort -committerdate --format %(refname)%00%(objectname)%00%(*objectname) [80ms]
2025-08-27 13:35:09.619 [info] > git status -z -uall [88ms]
2025-08-27 13:35:16.169 [info] > git hash-object -t tree /dev/null [82ms]
2025-08-27 13:35:16.264 [info] > git diff-tree -r --name-status -z --diff-filter=ADMR --find-renames=50% 4b825dc642cb6eb9a060e54bf8d69288fbee4904 2e88bccfb4ebe8df2cdd22f815dabfd847124e18 [86ms]
2025-08-27 13:35:16.900 [info] > git check-ignore -v -z --stdin [100ms]
2025-08-27 13:35:22.692 [info] > git show --textconv 2e88bccfb4ebe8df2cdd22f815dabfd847124e18:new_program.py [97ms]
2025-08-27 13:35:22.701 [info] > git ls-tree -l 2e88bccfb4ebe8df2cdd22f815dabfd847124e18 -- new_program.py [84ms]
2025-08-27 13:35:23.252 [info] > git check-ignore -v -z --stdin [97ms]
2025-08-27 13:35:25.634 [info] > git push [63ms]
2025-08-27 13:35:25.634 [info] fatal: No configured push destination.
Either specify the URL from the command-line or configure a remote repository using

    git remote add <name> <url>

and then push using the remote name

    git push <name>
2025-08-27 13:35:25.712 [info] > git config --get commit.template [72ms]
2025-08-27 13:35:25.719 [info] > git for-each-ref --format=%(refname)%00%(upstream:short)%00%(objectname)%00%(upstream:track)%00%(upstream:remotename)%00%(upstream:remoteref) --ignore-case refs/heads/main refs/remotes/main [74ms]
2025-08-27 13:35:25.800 [info] > git status -z -uall [77ms]
2025-08-27 13:35:25.806 [info] > git for-each-ref --sort -committerdate --format %(refname)%00%(objectname)%00%(*objectname) [79ms]
2025-08-27 13:35:27.804 [info] > git ls-tree -l 2e88bccfb4ebe8df2cdd22f815dabfd847124e18 -- new_program.py [52ms]
2025-08-27 13:35:42.103 [info] > git show --textconv 2e88bccfb4ebe8df2cdd22f815dabfd847124e18:new_program.py [67ms]
2025-08-27 13:35:42.104 [info] > git ls-tree -l 2e88bccfb4ebe8df2cdd22f815dabfd847124e18 -- new_program.py [56ms]
