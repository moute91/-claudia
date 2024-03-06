name: Test project
on: push
jobs: 
  test:
    runs-on: ubuntu-latest
    steps: 
      - name: Get code
        uses: action/checkout@v3
      - name: Install node-version
        uses: action/setup-node@v3   
        with:
          node-version: 18
      - name: Install dependency    
        run: npm ci
      - name: Run test    
        run: npm test
