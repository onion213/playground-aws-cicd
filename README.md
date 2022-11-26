# playground-aws-cicd
AWS Code シリーズを使った CICD 環境を構築してみる

# Usage
## Mirroring 設定
1. CodeCommit に Repo と Mirroring 用の IAM User 作成
    ```
    $ aws cloudformation deploy --template-file ./pipeline/repository.yaml --stack-name PlayCodePipeline-Repo --capabilities CAPABILITY_NAMED_IAM
    ```

2. Mirroring 用の キーペア作成
    ```
    $ ssh-keygen -t rsa -b 4096
    ```

    NOTE: 2022/11/26 時点では，AWS は RSA にしか対応指定なさそう． 
    https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_ssh-keys.html?icmpid=docs_iam_console#ssh-keys-code-commit

3. 公開鍵を AWS に登録
    ```
    $ aws iam upload-ssh-public-key  --user-name CodeCommitMirroringUser --ssh-public-key-body fileb://<先ほど作成した公開鍵のパス>
    ```

4. 秘密鍵と AWS 上で生成された 秘密鍵 ID を GitHub に登録
    ```
    $ gh secret set -r onion/playground-aws-cicd CODECOMMIT_SSH_PRIVATE_KEY --body "$(cat <先ほど作成した秘密鍵のパス>)"
    $ gh secret set -r onion/playground-aws-cicd CODECOMMIT_SSH_PRIVATE_KEY_ID --body "<公開鍵を AWS に登録した際に返ってきた `SSHPublicKeyBody`>" 
    ```


ここまでの設定で， GitHub に push した際に， GitHub Actions で作成した AWS CodeCommit 上の repository にも同内容が push されるようになる．
