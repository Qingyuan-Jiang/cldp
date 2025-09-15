# How to Enable GitHub Pages for Anonymous Academic Submission

This repository now contains a complete anonymous academic submission page for the CLDP project. Follow these steps to make it live:

## 1. Enable GitHub Pages

1. Go to your repository on GitHub
2. Click on **Settings** tab
3. Scroll down to **Pages** section in the left sidebar
4. Under **Source**, select **Deploy from a branch**
5. Choose **main** (or **master**) branch
6. Select **/ (root)** as the folder
7. Click **Save**

## 2. Access Your Site

After enabling, your site will be available at:
```
https://[your-username].github.io/cldp/
```

The GitHub Actions workflow will automatically build and deploy the site whenever you push changes.

## 3. Site Features

✅ **Anonymous Design**: No author information or institutional affiliations
✅ **Professional Layout**: Clean, academic-style presentation
✅ **Complete Content**: Abstract, methodology, results, and technical details
✅ **Responsive Design**: Works on desktop, tablet, and mobile
✅ **SEO Optimized**: Proper meta tags and structure

## 4. Customization

To customize the content:

- **Main Content**: Edit `index.html`
- **Site Configuration**: Edit `_config.yml`
- **Additional Pages**: Add new `.html` or `.md` files
- **Styling**: Modify the CSS in the `<style>` section of `index.html`

## 5. For Academic Review

This page is specifically designed for anonymous academic review:

- ✅ **Anonymous Submission Notice**: Clear banner indicating anonymous submission
- ✅ **Technical Focus**: Emphasis on methodology and results rather than authors
- ✅ **Professional Presentation**: Academic-quality layout and content organization
- ✅ **Contact Placeholder**: Anonymous contact information for review process

## 6. Local Testing

To test changes locally before publishing:

```bash
# Install Jekyll (if not already installed)
gem install jekyll bundler

# Navigate to your repository
cd /path/to/cldp

# Serve locally
jekyll serve

# Open http://localhost:4000 in your browser
```

## 7. Maintenance

The site will automatically update when you:
- Push changes to the main branch
- Modify any HTML, CSS, or configuration files
- The GitHub Actions workflow will handle the deployment

## Support

For any issues or questions about the site setup, refer to:
- GitHub Pages documentation: https://docs.github.com/en/pages
- Jekyll documentation: https://jekyllrb.com/docs/
- The `docs/README.md` file in this repository