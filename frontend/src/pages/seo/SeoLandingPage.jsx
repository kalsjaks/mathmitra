import React from 'react';
import { Navigate, useParams, useLocation } from 'react-router-dom';
import { SEO_PAGES_DATA } from './seoPagesData';
import SeoPageLayout from '../../components/seo/SeoPageLayout';

export default function SeoLandingPage({ slug: propSlug }) {
  const { slug: paramSlug } = useParams();
  const location = useLocation();

  // Determine slug from prop, param, or pathname
  const currentSlug = propSlug || paramSlug || location.pathname.replace(/^\//, '');
  const pageData = SEO_PAGES_DATA[currentSlug];

  if (!pageData) {
    return <Navigate to="/" replace />;
  }

  return <SeoPageLayout pageData={pageData} />;
}
