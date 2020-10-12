# financial-sanctions


## Requirements

1. Install git

https://git-scm.com/book/en/v2/Getting-Started-Installing-Git


2. Install docker

https://docs.docker.com/docker-for-mac/install/

3. Install docker-compose

https://docs.docker.com/compose/install/

## how to use

1. Clone the repository

```bash
git clone https://github.com/rmilosic/financial-sanctions.git
```
2. Placing source files


- Move to the cloned repository in terminal
- in `data` folder, place source files inside `source_files` subfolder

- **Naming**

    - EU file: `consolidated-EU.xml`
    - UN file: `consolidated-UN.xml`
    - US file: `consolidated-US.xml`


3. Running the consolidator script

```bash
docker-compose up --build
```

Output file `output_consolidated.xml` will be saved to folder `/data/output_files`

4. Restarting the consolidator script

```bash
docker-compose rm -s && docker-compose up --build
```

## Issues/bugs

Please report any issues or bugs.